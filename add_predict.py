import csv

rows = []
with open('standardized_data_calculated.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        row = []
        for entry in lines: 
            row.append(entry)
        row.append(float(lines[5]) * 5.800535091607343 + 31.81252666653501)
        rows.append(row)
    print(rows)
        
with open('standardized_data_calculated.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

