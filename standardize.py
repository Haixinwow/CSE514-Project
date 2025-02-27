import csv

sum = 0
sum_list = [0, 0, 0, 0, 0, 0, 0, 0]
with open('Concrete_Data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        for x, entry in enumerate (lines): 
            if x == 8: 
                break
            sum_list[x] += float(lines[x])
    for x, sum in enumerate (sum_list): 
        sum_list[x] = sum / 1030
mean = sum / 1030
# print (sum_list)

standard_deviation = [0, 0, 0, 0, 0, 0, 0, 0]
with open('Concrete_Data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  next(csvFile, None)
  for lines in csvFile:
        # print(lines)
        for x, entry in enumerate(lines): 
            if x == 8: 
                break
            standard_deviation[x] += (float(entry) - sum_list[x]) ** 2
        # numerator += (float(lines[0]) - mean) ** 2

import math
for i, entry in enumerate(standard_deviation): 
    standard_deviation[i] = math.sqrt(entry/1030) 

print("mean: ", sum_list)
print ("standard deviation: ", standard_deviation)


with open('standardized_data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        for x, entry in enumerate(lines): 
            if x == 8: 
                print (float(entry))
            else: 
                break
                # print ((float(entry) - sum_list[x])/ standard_deviation[x])

rows = []
with open('standardized_data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for i, r in enumerate(csvFile):
        if i == 0: 
            row = []
            for column in r:
                row.append(column)
            # print ("THE ROW: ", row)
            rows.append(row)
            # print("rows now: ", rows)
        else: 
            row = []
            for j, column in enumerate(r):
                if j == 8: 
                    row.append(float(column))
                else:
                    row.append((float(column) - sum_list[j])/ standard_deviation[j])
            # print(row)
            rows.append(row)
            # print("done appending")
    # print ("THE FINAL ROWS: ", rows)
# with open('standardized_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# print(lines)
# print("standard deviation: ", math.sqrt(numerator/1030))