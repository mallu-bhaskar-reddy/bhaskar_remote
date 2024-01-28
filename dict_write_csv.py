import csv
with open('data/employee_dict_file.csv','w') as csv_file:

    fields =['name','department','birth']

    employee_writer = csv.DictWriter(csv_file,fieldnames=fields)

    employee_writer.writeheader()
    employee_writer.writerow({'name':'Jhon Smith', 'department': 'Admin','birth':'Nov'})
    employee_writer.writerow({'name':'Bhaskar Reddy', 'department': 'IT','birth':'May'})