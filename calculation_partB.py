import csv
import math

# mean:  [281.1678640776696, 73.89582524271844, 54.18834951456309, 181.56728155339803, 6.204660194174757, 972.9189320388344, 773.5804854368922, 45.662135922330094]
# standard deviation:  [104.45562093052506, 86.23744840174245, 63.96593010174097, 21.34384992224351, 5.970940765272748, 77.71620016310318, 80.13705031241201, 63.13923912883348]

mse = 0
variance = 0
# sum = 0
the_list = []

with open('standardized_raw_training.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        the_list.append((float(lines[5]), float(lines[8])))

def calculation_multi(list, alpha):
    m_old = 1
    b_old = 1
    # mse_temp = math.inf
    
    for i in range (1):
        sum_m = 0.0
        sum_b = 0.0
        # mse_sum = 0.0

        for predictor, response in list:

            predict_y = m_old * predictor + b_old
            error = response - predict_y

            sum_m += -2 * error * predictor
            sum_b += -2 * error
            # print("sum m and sum b: ", sum_m, sum_b)

        print("length: ", len(list))

        m_old -= alpha * (sum_m / len(list))
        b_old -= alpha * (sum_b / len(list))
        
        
        # for predictor, response in list: 
        #     predict_y = m_old * predictor + b_old
        #     error = response - predict_y
        #     mse_sum += error ** 2
        
        # mse_temp = mse_sum / len(list)
        # print("mse_temp: " , mse_temp)

    return (m_old, b_old)
# learning curve for standardized: 0.001
# learning curve for raw: 0.000006
m_and_b = calculation_multi(the_list, 0.000006)
print("m and b: ", m_and_b)


testing_list = []
just_y_list = []
with open('standardized-raw-testing.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        # sum += float(lines[8])
        y_true = float(lines[9])
        print(y_true)
        x_test = float(lines[5])
        just_y_list.append(y_true)
        predict = x_test * m_and_b[0] + m_and_b[1]
        testing_list.append((predict, y_true))
    
# print ("mean: ", sum/129)
# Found out about the sum function on geeksforgeeks: https://www.geeksforgeeks.org/sum-function-python/
y_mean = sum(just_y_list) / len(testing_list)

# with open('standardized-raw-testing.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     next(csvFile, None)
#     for lines in csvFile:
#         predict = float(lines[8]) * m_and_b[0] + m_and_b[1]
#         variance += ((sum / 129) - float(lines[8])) ** 2
#         mse += (predict - float(lines[9])) ** 2

mse = sum((y_pred - y_true) ** 2 for y_pred, y_true in testing_list) / len(testing_list)
variance = sum((y_true - y_mean) ** 2 for y_true in just_y_list) / len(just_y_list)


print("mean: ", y_mean)
print ("MSE: ", mse)
print ("variance: ", variance)
print("variance explained: ", 1 - (mse / variance))




# import numpy as np 
# import pandas as pd 
# import seaborn as sns 
# import matplotlib.pyplot as plt 
# from sklearn import preprocessing, svm 
# from sklearn.model_selection import train_test_split 
# from sklearn.linear_model import LinearRegression 

# x_axis = []
# y_axis = []
# with open('standardized_data.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     next(csvFile, None)
#     for lines in csvFile:
#         # sum += float(lines[8])
#         y_true = float(lines[8])
#         x_test = float(lines[5])
       
#         predict = x_test * 5.800535091607343 + 31.81252666653501
#         x_axis.append(x_test)
#         y_axis.append(predict)

# x = np.array(x_axis)
# y = np.array(y_axis)

# plt.scatter(x, y)
# plt.show()
