import csv

def csvJob():
    pass
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
def csvName():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['AAA BBB', 'Ceo', 'November'])
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
        employee_writer.writerow(['Jame Mar', 'IT', 'March'])
        employee_writer.writerow(['Omega migell', 'Manager', 'Feb'])
csvName()