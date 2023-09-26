# Author - Manpreet Dhindsa
# Data Converter
# Reads raw data from predict+students+dropout+and+academic+success\\data.csv and outputs formatted_data.csv
# formatted_data.csv is ready for pre-processing

import csv

def convert():
    input_file_path = "predict+students+dropout+and+academic+success\\data.csv"
    output_file_path = "formatted_data.csv"

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        header_row = input_file.readline().strip().split(';')
        
        output_file.write(','.join(header_row) + '\n')

        for line in input_file:
            data = line.strip().split(';')
            output_file.write(','.join(data) + '\n')

    print("Data has been formatted and saved to 'formatted_data.csv'.")

def main():
    convert()

if __name__ == "__main__":
    main()
    