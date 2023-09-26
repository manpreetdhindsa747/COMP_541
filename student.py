# Author - Manpreet Dhindsa

class Student:
    def __init__(self, marital_status, application_mode, application_order, course, daytimeevening_attendance,
                 previous_qualification, previous_qualification_grade, nacionality, mothers_qualification,
                 fathers_qualification, mothers_occupation, fathers_occupation, admission_grade, displaced,
                 educational_special_needs, debtor, tuition_fees_up_to_date, gender, scholarship_holder,
                 age_at_enrollment, international, curricular_units_1st_sem_credited,
                 curricular_units_1st_sem_enrolled, curricular_units_1st_sem_evaluations,
                 curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
                 curricular_units_1st_sem_without_evaluations, curricular_units_2nd_sem_credited,
                 curricular_units_2nd_sem_enrolled, curricular_units_2nd_sem_evaluations,
                 curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
                 curricular_units_2nd_sem_without_evaluations, unemployment_rate, inflation_rate, gdp, target):
        self.marital_status = marital_status
        self.application_mode = application_mode
        self.application_order = application_order
        self.course = course
        self.daytimeevening_attendance = daytimeevening_attendance
        self.previous_qualification = previous_qualification
        self.previous_qualification_grade = previous_qualification_grade
        self.nacionality = nacionality
        self.mothers_qualification = mothers_qualification
        self.fathers_qualification = fathers_qualification
        self.mothers_occupation = mothers_occupation
        self.fathers_occupation = fathers_occupation
        self.admission_grade = admission_grade
        self.displaced = displaced
        self.educational_special_needs = educational_special_needs
        self.debtor = debtor
        self.tuition_fees_up_to_date = tuition_fees_up_to_date
        self.gender = gender
        self.scholarship_holder = scholarship_holder
        self.age_at_enrollment = age_at_enrollment
        self.international = international
        self.curricular_units_1st_sem_credited = curricular_units_1st_sem_credited
        self.curricular_units_1st_sem_enrolled = curricular_units_1st_sem_enrolled
        self.curricular_units_1st_sem_evaluations = curricular_units_1st_sem_evaluations
        self.curricular_units_1st_sem_approved = curricular_units_1st_sem_approved
        self.curricular_units_1st_sem_grade = curricular_units_1st_sem_grade
        self.curricular_units_1st_sem_without_evaluations = curricular_units_1st_sem_without_evaluations
        self.curricular_units_2nd_sem_credited = curricular_units_2nd_sem_credited
        self.curricular_units_2nd_sem_enrolled = curricular_units_2nd_sem_enrolled
        self.curricular_units_2nd_sem_evaluations = curricular_units_2nd_sem_evaluations
        self.curricular_units_2nd_sem_approved = curricular_units_2nd_sem_approved
        self.curricular_units_2nd_sem_grade = curricular_units_2nd_sem_grade
        self.curricular_units_2nd_sem_without_evaluations = curricular_units_2nd_sem_without_evaluations
        self.unemployment_rate = unemployment_rate
        self.inflation_rate = inflation_rate
        self.gdp = gdp
        self.target = target

    def __repr__(self):
        return f"Student(" \
               f"marital_status={self.marital_status}, " \
               f"application_mode={self.application_mode}, " \
               f"application_order={self.application_order}, " \
               f"course={self.course}, " \
               f"daytimeevening_attendance={self.daytimeevening_attendance}, " \
               f"previous_qualification={self.previous_qualification}, " \
               f"previous_qualification_grade={self.previous_qualification_grade}, " \
               f"nacionality={self.nacionality}, " \
               f"mothers_qualification={self.mothers_qualification}, " \
               f"fathers_qualification={self.fathers_qualification}, " \
               f"mothers_occupation={self.mothers_occupation}, " \
               f"fathers_occupation={self.fathers_occupation}, " \
               f"admission_grade={self.admission_grade}, " \
               f"displaced={self.displaced}, " \
               f"educational_special_needs={self.educational_special_needs}, " \
               f"debtor={self.debtor}, " \
               f"tuition_fees_up_to_date={self.tuition_fees_up_to_date}, " \
               f"gender={self.gender}, " \
               f"scholarship_holder={self.scholarship_holder}, " \
               f"age_at_enrollment={self.age_at_enrollment}, " \
               f"international={self.international}, " \
               f"curricular_units_1st_sem_credited={self.curricular_units_1st_sem_credited}, " \
               f"curricular_units_1st_sem_enrolled={self.curricular_units_1st_sem_enrolled}, " \
               f"curricular_units_1st_sem_evaluations={self.curricular_units_1st_sem_evaluations}, " \
               f"curricular_units_1st_sem_approved={self.curricular_units_1st_sem_approved}, " \
               f"curricular_units_1st_sem_grade={self.curricular_units_1st_sem_grade}, " \
               f"curricular_units_1st_sem_without_evaluations={self.curricular_units_1st_sem_without_evaluations}, " \
               f"curricular_units_2nd_sem_credited={self.curricular_units_2nd_sem_credited}, " \
               f"curricular_units_2nd_sem_enrolled={self.curricular_units_2nd_sem_enrolled}, " \
               f"curricular_units_2nd_sem_evaluations={self.curricular_units_2nd_sem_evaluations}, " \
               f"curricular_units_2nd_sem_approved={self.curricular_units_2nd_sem_approved}, " \
               f"curricular_units_2nd_sem_grade={self.curricular_units_2nd_sem_grade}, " \
               f"curricular_units_2nd_sem_without_evaluations={self.curricular_units_2nd_sem_without_evaluations}, " \
               f"unemployment_rate={self.unemployment_rate}, " \
               f"inflation_rate={self.inflation_rate}, " \
               f"gdp={self.gdp}, " \
               f"target={self.target})"
    