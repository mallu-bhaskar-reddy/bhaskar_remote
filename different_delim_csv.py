import csv

with open('data/different_delim.csv') as csv_file:
    file = csv.DictReader(csv_file, delimiter ='|')
    line_count = 0
    for row in file:
        if line_count == 0:
            print(f"Column names are {','.join(row)}")
            line_count += 1
        
        print(f"{row['name']} lives at {row['address']} and joined on {row['date joined']}")
        line_count += 1
    
    print(f'processed {line_count} lines')