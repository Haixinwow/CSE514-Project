import csv
import math

# x1 = [3, 4, 10, 3, 11]
# x2 = [4, 2, 2, 4, 1]
# x3 = [4, 1, 5, 5, 1]
# y = [3, 2, 8, 4, 5]

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
y = []

with open('raw_training.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        x1.append(float(lines[0]))
        x2.append(float(lines[1]))
        x3.append(float(lines[2]))
        x4.append(float(lines[3]))
        x5.append(float(lines[4]))
        x6.append(float(lines[5]))
        x7.append(float(lines[6]))
        x8.append(float(lines[7]))
        y.append(float(lines[8]))
# print(y)

def multivariate_linear_regression(x1, x2, x3, x4, x5, x6, x7, x8, y, alpha): 
    m_1 = 1
    m_2 = 1
    m_3 = 1
    m_4 = 1
    m_5 = 1
    m_6 = 1
    m_7 = 1
    m_8 = 1
    b = 1
    # print("alpha: ", alpha)

    for i in range (1000):
        sum_m1 = 0.0
        sum_m2 = 0.0
        sum_m3 = 0.0
        sum_m4 = 0.0
        sum_m5 = 0.0
        sum_m6 = 0.0
        sum_m7 = 0.0
        sum_m8 = 0.0
        sum_b = 0.0

        for index, response in enumerate (y):
       
            predict_y = m_1 * x1[index] + m_2 * x2[index] + m_3 * x3[index] + m_4 * x4[index] + m_5 * x5[index] + m_6 * x6[index] + m_7 * x7[index] + m_8 * x8[index] + b
            error = response - predict_y
            # print("error", error)

            sum_m1 += -2 * error * x1[index]
            sum_m2 += -2 * error * x2[index]
            sum_m3 += -2 * error * x3[index]
            sum_m4 += -2 * error * x4[index]
            sum_m5 += -2 * error * x5[index]
            sum_m6 += -2 * error * x6[index]
            sum_m7 += -2 * error * x7[index]
            sum_m8 += -2 * error * x8[index]
            sum_b += -2 * error

        m_1 -= (alpha * sum_m1/len(y))
        m_2 -= (alpha * sum_m2/len(y))
        m_3 -= (alpha * sum_m3/len(y))
        m_4 -= (alpha * sum_m4/len(y))
        m_5 -= (alpha * sum_m5/len(y))
        m_6 -= (alpha * sum_m6/len(y))
        m_7 -= (alpha * sum_m7/len(y))
        m_8 -= (alpha * sum_m8/len(y))
        b -= (alpha * sum_b/len(y))

    return (m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8, b)
    


result = multivariate_linear_regression(x1, x2, x3, x4, x5, x6, x7, x8, y, 0.000000583)

print("m1: ", result[0])
print("m2: ", result[1])
print("m3: ", result[2])
print("m4: ", result[3])
print("m5: ", result[4])
print("m6: ", result[5])
print("m7: ", result[6])
print("m8: ", result[7])
print("b: ", result[8])


testing_list = []
just_y_list = []
with open('raw_testing.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    for lines in csvFile:
        y_true = float(lines[8])
        # print(y_true)
        just_y_list.append(y_true)
        predict = float(lines[0]) * result[0] + float(lines[1]) * result[1] + float(lines[2]) * result[2] + float(lines[3]) * result[3] + float(lines[4]) * result[4] + float(lines[5]) * result[5] + float(lines[6]) * result[6] + float(lines[7]) * result[7] + result[8]
        testing_list.append((predict, y_true))
    
y_mean = sum(just_y_list) / len(testing_list)

mse = sum((y_pred - y_true) ** 2 for y_pred, y_true in testing_list) / len(testing_list)
variance = sum((y_true - y_mean) ** 2 for y_true in just_y_list) / len(just_y_list)


print("mean: ", y_mean)
print ("MSE: ", mse)
print ("variance: ", variance)
print("variance explained: ", 1 - (mse / variance))