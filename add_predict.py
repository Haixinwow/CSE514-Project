import csv

rows = []

# m1:  13.801121792519275
# m2:  10.726507981891228
# m3:  6.7616339062406645
# m4:  -2.8872461041481956
# m5:  0.7083611018094296
# m6:  2.1915060265257305
# m7:  2.678510081694333
# m8:  7.505350507347406
# b:  36.52415511208455

# with open('standardized_data_calculated.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     next(csvFile, None)
#     for lines in csvFile:
#         row = []
#         for entry in lines: 
#             row.append(entry)
#         row.append(float(lines[5]) * 5.800535091607343 + 31.81252666653501)
#         rows.append(row)
#     print(rows)
        
# with open('standardized_data_calculated.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# with open('standardized_data_calculated_multivariate.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     next(csvFile, None)
#     for lines in csvFile:
#         row = []
#         for entry in lines: 
#             row.append(entry)
#         row.append(float(lines[1]) * 13.801121792519275 + float(lines[2]) * 10.726507981891228 + float(lines[3]) * 6.7616339062406645 + float(lines[4]) * -2.8872461041481956 + float(lines[5]) * 0.7083611018094296 + float(lines[6]) * 2.1915060265257305 + float(lines[7]) * 2.678510081694333 + float(lines[8]) * 7.505350507347406 + 36.52415511208455)
#         rows.append(row)
#     print(rows)
        
# with open('standardized_data_calculated_multivariate.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

with open('raw_training_statsmodel.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        row = []
        for entry in lines: 
            row.append(entry)
        row.append(float(lines[1]) * -1.0557 + float(lines[2]) * -1.2710 + float(lines[3]) * -2.4555 + float(lines[4]) * 0.0877 + float(lines[5]) * -0.7082 + float(lines[6]) * -0.8863 + float(lines[7]) * -0.1681 + float(lines[8]) * 1.3241 + 2207.0176)
        rows.append(row)
    # print(rows)




testing_list = []
just_y_list = []
with open('raw_training_statsmodel.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        y_true = float(lines[8])
        # print(y_true)
        just_y_list.append(y_true)
        predict = float(lines[1]) * -1.0557 + float(lines[2]) * -1.2710 + float(lines[3]) * -2.4555 + float(lines[4]) * 0.0877 + float(lines[5]) * -0.7082 + float(lines[6]) * -0.8863 + float(lines[7]) * -0.1681 + float(lines[8]) * 1.3241 + 2207.0176
        testing_list.append((predict, y_true))
    
y_mean = sum(just_y_list) / len(testing_list)

mse = sum((y_pred - y_true) ** 2 for y_pred, y_true in testing_list) / len(testing_list)
variance = sum((y_true - y_mean) ** 2 for y_true in just_y_list) / len(just_y_list)


print("mean: ", y_mean)
print ("MSE: ", mse)
print ("variance: ", variance)
print("variance explained: ", 1 - (mse / variance))

        
# with open('standardized_data_calculated_multivariate.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)
