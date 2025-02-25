import csv

sum = 0
sum_list = []
with open('Concrete_Data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  next(csvFile, None)
  s = 0
  for lines in csvFile:
        sum += float(lines[0])
mean = sum / 1030

numerator = 0
with open('Concrete_Data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  next(csvFile, None)
  for lines in csvFile:
        # print(lines)
        numerator += (float(lines[0]) - mean) ** 2

import math

print(mean)
print(math.sqrt(numerator/1030))

with open('Concrete_Data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  next(csvFile, None)
  for lines in csvFile:
        # print(lines)
        print ((float(lines[0]) - mean)/ math.sqrt(numerator/1030))

print(mean)
print("standard deviation: ", math.sqrt(numerator/1030))