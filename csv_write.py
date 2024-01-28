import csv

with open('data/employee_file_2.csv', 'w') as csv_file:
    employee_writer = csv.writer(csv_file, delimiter= ',', quotechar='"',quoting=csv.QUOTE_NONE, escapechar= '|')

    employee_writer.writerow(['Jhon Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Bhaskar Reddy','IT','May'])