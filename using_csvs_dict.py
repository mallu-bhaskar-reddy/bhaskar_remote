import csv

with open('data/employee_birthday.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
        
        line_count += 1
        
    print(f'Processed line count {line_count} lines')