# Author - Manpreet Dhindsa
# Data Processor
# Reads formatted data from formatted_data.csv and outputs processed_data.csv
# processed_data.csv is ready for analysis using jupyter

import csv
import re
import shutil
import openpyxl

#region Dictionaries
# Column 1 (A)
marital_status = {
    1: "single",
    2: "married",
    3: "widower",
    4: "divorced",
    5: "facto_union",
    6: "legally_separated"
}

# Column 2 (B)
application_mode = {
    1: "first_phase_general_contingent",
    2: "ordinance_no_612_93",
    5: "first_phase_special_contingent_azores_island",
    7: "holders_of_other_higher_courses",
    10: "ordinance_no_854_B_99",
    15: "international_student_bachelor",
    16: "first_phase_special_contingent_Madeira_island",
    17: "second_phase_general_contingent",
    18: "third_phase_general_contingent",
    26: "ordinance_no_533_A_99_item_b2_different_plan",
    27: "ordinance_no_533_A_99_item_b3_other_institution",
    39: "over_23_years_old",
    42: "transfer",
    43: "change_of_course",
    44: "technological_specialization_diploma_holders",
    51: "change_of_institution_course",
    53: "short_cycle_diploma_holders",
    57: "change_of_institution_course_international"
}

# Column 3 (C) 0-9 (0 denoted first choice and 9 denotes last choice)

# Column 4 (D)
course = {
    33: 'biofuel_production_technologies',
    171: 'animation_and_multimedia_design',
    8014: 'social_service_evening_attendance',
    9003: 'agronomy',
    9070: 'communication_design',
    9085: 'veterinary_nursing',
    9119: 'informatics_engineering',
    9130: 'equinculture',
    9147: 'management',
    9238: 'social_service',
    9254: 'tourism',
    9500: 'nursing',
    9556: 'oral_hygiene',
    9670: 'advertising_and_marketing_management',
    9773: 'journalism_and_communication',
    9853: 'basic_education',
    9991: 'management_evening_attendance'
}

# Column 5 (E) - 1 denotes daytime attendance and 0 is evening
daytime_attendance = {
    1: True,
    0: False
}

# Column 6 (F)
previous_qualification = {
    1: 'secondary_education',
    2: 'higher_education_bachelors_degree',
    3: 'higher_education_degree',
    4: 'higher_education_masters',
    5: 'higher_education_doctorate',
    6: 'frequency_of_higher_education',
    9: 'twelfth_year_of_schooling_not_completed',
    10: 'elevnth_year_of_schooling_not_completed',
    12: 'other_11th_year_of_schooling',
    14: 'tenth_year_of_schooling',
    15: 'tenth_year_of_schooling_not_completed',
    19: 'basic_education_3rd_cycle_9th10th11th_year_or_equiv',
    38: 'basic_education_2nd_cycle_6th7th8th_year_or_equiv',
    39: 'technological_specialization_course',
    40: 'higher_education_degree_1st_cycle',
    42: 'professional_higher_technical_course',
    43: 'higher_education_master_2nd_cycle'
}

# Column 7 (G) - Continuous denotes grade in previous qualification

# Column 8 (H)
nationality = {
    1: 'portuguese',
    2: 'german',
    6: 'spanish',
    11: 'italian',
    13: 'dutch',
    14: 'english',
    17: 'lithuanian',
    21: 'angolan',
    22: 'cape_verdean',
    24: 'guinean',
    25: 'mozambican',
    26: 'santomean',
    32: 'turkish',
    41: 'brazilian',
    62: 'romanian',
    100: 'moldova',
    101: 'mexican',
    103: 'ukrainian',
    105: 'russian',
    108: 'cuban',
    109: 'colombian'
}

# Column 9 (I)
mother_qualification = {
    1: 'secondary_education_12th_year_of_schooling_or_equiv',
    2: 'higher_education_bachelors_degree',
    3: 'higher_education_degree',
    4: 'higher_education_masters',
    5: 'higher_education_doctorate',
    6: 'frequency_of_higher_education',
    9: 'twelfth_year_of_schooling_not_completed',
    10: 'elevnth_year_of_schooling_not_completed',
    11: 'seventh_year_old',
    12: 'other_11th_year_of_schooling',
    14: 'tenth_year_of_schooling',
    18: 'general_commerce_course',
    19: 'basic_education_3rd_cycle_9th10th11th_year_or_equiv',
    22: 'technicalprofessional_course',
    26: 'seventh_year_of_schooling',
    27: 'second_cycle_of_the_general_high_school_course',
    29: 'ninth_year_of_schooling_not_completed',
    30: 'eigth_year_of_schooling',
    34: 'unknown',
    35: 'cant_read_or_write',
    36: 'can_read_without_having_a_4th_year_of_schooling',
    37: 'basic_education_1st_cycle_4th5th_year_or_equiv',
    38: 'basic_education_2nd_cycle_6th7th8th_year_or_equiv',
    39: 'technological_specialization_course',
    40: 'higher_education_degree_1st_cycle',
    41: 'specialized_higher_studies_course',
    42: 'professional_higher_technical_course',
    43: 'higher_education_master_2nd_cycle',
    44: 'higher_education_doctorate_3rd_cycle'
}

# Column 10 (J)
father_qualification = {
    1: 'secondary_education_12th_year_of_schooling_or_equiv',
    2: 'higher_education_bachelors_degree',
    3: 'higher_education_degree',
    4: 'higher_education_masters',
    5: 'higher_education_doctorate',
    6: 'frequency_of_higher_education',
    9: 'twelfth_year_of_schooling_not_completed',
    10: 'eleventh_year_of_schooling_not_completed',
    11: 'seventh_year_old',
    12: 'other_11th_year_of_schooling',
    13: 'second_year_complementary_high_school_course',
    14: 'tenth_year_of_schooling',
    18: 'general_commerce_course',
    19: 'basic_education_3rd_cycle_9th10th11th_year_or_equiv',
    20: 'complementary_high_school_course',
    22: 'technicalprofessional_course',
    25: 'complementary_high_school_course_not_concluded',
    26: 'seventh_year_of_schooling',
    27: 'second_cycle_of_the_general_high_school_course',
    29: 'ninth_year_of_schooling_not_completed',
    30: 'eighth_year_of_schooling',
    31: 'general_course_of_administration_and_commerce',
    33: 'supplementary_accounting_and_administration',
    34: 'unknown',
    35: 'cant_read_or_write',
    36: 'can_read_without_having_a_4th_year_of_schooling',
    37: 'basic_education_1st_cycle_4th5th_year_or_equiv',
    38: 'basic_education_2nd_cycle_6th7th8th_year_or_equiv',
    39: 'technological_specialization_course',
    40: 'higher_education_degree_1st_cycle',
    41: 'specialized_higher_studies_course',
    42: 'professional_higher_technical_course',
    43: 'higher_education_master_2nd_cycle',
    44: 'higher_education_doctorate_3rd_cycle'
}

# Column 11 (K)
mother_occupation = {
    0: 'student',
    1: 'representatives_of_the_legislative_power_and_executive_bodies_directors_directors_and_executive_managers',
    2: 'specialists_in_intellectual_and_scientific_activities',
    3: 'intermediate_level_technicians_and_professions',
    4: 'administrative_staff',
    5: 'personal_services_security_and_safety_workers_and_sellers',
    6: 'farmers_and_skilled_workers_in_agriculture_fisheries_and_forestry',
    7: 'skilled_workers_in_industry_construction_and_craftsmen',
    8: 'installation_and_machine_operators_and_assembly_workers',
    9: 'unskilled_workers',
    10: 'armed_forces_professions',
    90: 'other_situation',
    99: 'blank',
    122: 'health_professionals',
    123: 'teachers',
    125: 'specialists_in_information_and_communication_technologies_ict',
    131: 'intermediate_level_science_and_engineering_technicians_and_professions',
    132: 'technicians_and_professionals_of_intermediate_level_of_health',
    134: 'intermediate_level_technicians_from_legal_social_sports_cultural_and_similar_services',
    141: 'office_workers_secretaries_in_general_and_data_processing_operators',
    143: 'data_accounting_statistical_financial_services_and_registry_related_operators',
    144: 'other_administrative_support_staff',
    151: 'personal_service_workers',
    152: 'sellers',
    153: 'personal_care_workers_and_the_like',
    171: 'skilled_construction_workers_and_the_like_except_electricians',
    173: 'skilled_workers_in_printing_precision_instrument_manufacturing_jewelers_artisans_and_the_like',
    175: 'workers_in_food_processing_woodworking_clothing_and_other_industries_and_crafts',
    191: 'cleaning_workers',
    192: 'unskilled_workers_in_agriculture_animal_production_fisheries_and_forestry',
    193: 'unskilled_workers_in_extractive_industry_construction_manufacturing_and_transport',
    194: 'meal_preparation_assistants'
}

# Column 12 (J)
father_occupation = {
    0: 'student',
    1: 'representatives_of_the_legislative_power_and_executive_bodies_directors_directors_and_executive_managers',
    2: 'specialists_in_intellectual_and_scientific_activities',
    3: 'intermediate_level_technicians_and_professions',
    4: 'administrative_staff',
    5: 'personal_services_security_and_safety_workers_and_sellers',
    6: 'farmers_and_skilled_workers_in_agriculture_fisheries_and_forestry',
    7: 'skilled_workers_in_industry_construction_and_craftsmen',
    8: 'installation_and_machine_operators_and_assembly_workers',
    9: 'unskilled_workers',
    10: 'armed_forces_professions',
    90: 'other_situation',
    99: 'blank',
    101: 'armed_forces_officers',
    102: 'armed_forces_sergeants',
    103: 'other_armed_forces_personnel',
    112: 'directors_of_administrative_and_commercial_services',
    114: 'hotel_catering_trade_and_other_services_directors',
    121: 'specialists_in_the_physical_sciences_mathematics_engineering_and_related_techniques',
    122: 'health_professionals',
    123: 'teachers',
    124: 'specialists_in_finance_accounting_administrative_organization_public_and_commercial_relations',
    131: 'intermediate_level_science_and_engineering_technicians_and_professions',
    132: 'technicians_and_professionals_of_intermediate_level_of_health',
    134: 'intermediate_level_technicians_from_legal_social_sports_cultural_and_similar_services',
    135: 'information_and_communication_technology_technicians',
    141: 'office_workers_secretaries_in_general_and_data_processing_operators',
    143: 'data_accounting_statistical_financial_services_and_registry_related_operators',
    144: 'other_administrative_support_staff',
    151: 'personal_service_workers',
    152: 'sellers',
    153: 'personal_care_workers_and_the_like',
    154: 'protection_and_security_services_personnel',
    161: 'market_oriented_farmers_and_skilled_agricultural_and_animal_production_workers',
    163: 'farmers_livestock_keepers_fishermen_hunters_and_gatherers_subsistence',
    171: 'skilled_construction_workers_and_the_like_except_electricians',
    172: 'skilled_workers_in_metallurgy_metalworking_and_similar',
    174: 'skilled_workers_in_electricity_and_electronics',
    175: 'workers_in_food_processing_woodworking_clothing_and_other_industries_and_crafts',
    181: 'fixed_plant_and_machine_operators',
    182: 'assembly_workers',
    183: 'vehicle_drivers_and_mobile_equipment_operators',
    192: 'unskilled_workers_in_agriculture_animal_production_fisheries_and_forestry',
    193: 'unskilled_workers_in_extractive_industry_construction_manufacturing_and_transport',
    194: 'meal_preparation_assistants',
    195: 'street_vendors_except_food_and_street_service_providers'
}

# Column 13 (M) - Admission Grade (Continuous)

# Column 14 (N) - Displaced	(1 – yes 0 – no)
displaced = {
    1: True,
    0: False
}

# Column 15 (O) - Educational Special Needs	(1 – yes 0 – no)
educational_special_needs = {
    1: True,
    0: False
}

# Column 16 (P) - Debtor (1 – yes 0 – no)
debtor = {
    1: True,
    0: False
}

# Column 17 (Q) - Tuition fees up to date (1 – yes 0 – no)
tuition_fees_up_to_date = {
    1: True,
    0: False
}

# Column 18 (R) - Gender (1 – male 0 – female)
gender = {
    1: "male",
    0: "female"
}

# Column 19 (S) - Scholarship (1 – yes 0 – no)
scholarship = {
    1: True,
    0: False
}

# Column 20 (T) - Age at enrollment (Continuous)

# Column 21 (U) - International Student (1 – yes 0 – no)
international = {
    1: True,
    0: False
}

# Column 22 (V) - Curricular units 1st sem (credited) - Integer

# Column 23 (W) - Curricular units 1st sem (enrolled) - Integer
 
# Column 24 (X) - Curricular units 1st sem (evaluations) - Integer

# Column 25 (Y) - Curricular units 1st sem (approved) - Integer

# Column 26 (Z) - Curricular units 1st sem (grade) - Integer

# Column 27 (AA) - Curricular units 1st sem (without evaluations) - Integer

# Column 28 (AB) - Curricular units 2nd sem (credited) - Integer

# Column 29 (AC) - Curricular units 2nd sem (enrolled) - Integer
 
# Column 30 (AD) - Curricular units 2nd sem (evaluations) - Integer
 
# Column 31 (AE) - Curricular units 2nd sem (approved) - Integer
 
# Column 32 (AF) - Curricular units 2nd sem (grade) - Integer
 
# Column 33 (AG) - Curricular units 2nd sem (without evaluations) - Integer

# Column 34 (AH) - Unemployment rate - Continuous
 
# Column 35 (AI) - Inflation rate - Continuous

# Column 36 (AJ) - GDP - Continuous

# Column 37 (AK) - Target - Categorical - (dropout, enrolled, and graduate)
#endregion

def format_cell_value(cell_value):
    return re.sub(r'[^a-zA-Z0-9_]', '', cell_value.replace(' ', '_')).lower()

def process_header():
    workbook = openpyxl.load_workbook('formatted_data.xlsx')
    sheet = workbook.active

    for cell in sheet[1]:
        cell.value = format_cell_value(str(cell.value))

    workbook.save('processed_data.xlsx')
    workbook.close()

def main():
    process_header()

if __name__ == "__main__":
    main()
    