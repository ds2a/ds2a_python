import csv

#CSV READING
with open("csv_file_1.csv",mode='w',newline='\n') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(["id","name"])
    file_writer.writerow(["1","abc"])
    file_writer.writerow(["2","def"])

#CSV WRITING
with open('csv_file_1.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

