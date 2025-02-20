
def calculation(x, y, alpha, m_old, b_old): 
    #y = mx + b
    predict_y = m_old * x + b_old
    error = y-predict_y

    #b_new = b_old - alpha * -2 * error 
    #m_new = m_old - alpha * -2 * error * x
    #got both formula from lecture slides 3 - Linear Regression and Gradient Descent.pdf page 27
    m_new = m_old - alpha * -2 * error * x
    b_new = b_old - alpha * -2 * error
    
    # print(predict_y)
    # print(error)

    print(m_new)
    print(b_new)

    return((m_new, b_new))


# calculation(3, 4, 0.1, 1, 1)
# calculation(540, 80, 0.1, 1, 1)

def calculation_multi(list, alpha, m_old, b_old, length): 
    sum_m = 0.0
    sum_b = 0.0
    
    for pair in list: 
        # result = calculation(pair[0], pair[1], alpha, m_old, b_old)
        predict_y = m_old * pair[0] + b_old
        error = pair[1]-predict_y

        sum_m += -2 * error * pair[0]
        sum_b += -2 * error

    # print("sums")
    # print(sum_m)
    # print(sum_b)

    average_m = sum_m/length
    average_b = sum_b/length
    # print("average")
    # print(average_m)
    # print(average_b)

    final_m = m_old - alpha * average_m
    final_b = b_old - alpha * average_b
        
    print("final")
    print(final_m)
    print(final_b)
    
# x = 3,  y = 3
# x = 4,  y = 2
# x = 10, y = 8
# list_1 = [(3, 3), (4, 2), (10, 8)]
# calculation_multi(list_1, 0.1, 1, 1, len(list_1))

# x = 3,   y = 3
# x = 4,   y = 2
# x = 10, y = 8
# x = 3,   y = 4
# x = 11,  y = 5
# list_2 = [(3, 3), (4, 2), (10, 8), (3, 4), (11, 5)]
# calculation_multi(list_2, 0.1, 1, 1, len(list_2))

# x = 540, y = 80
# x = 332, y = 40
# x = 266, y = 47
# list_3 = [(540, 80), (332, 40), (266, 47)]
# calculation_multi(list_3, 0.1, 1, 1, len(list_3))

# x = 540, y = 80
# x = 332, y = 40
# x = 266, y = 47
# x = 380, y = 44
# x = 199, y = 38
# list_4 = [(540, 80), (332, 40), (266, 47), (380, 44), (199, 38)]
# calculation_multi(list_4, 0.1, 1, 1, len(list_4))

# list_5 = [(540, 80), (332, 40), (266, 47), (380, 44), (199, 38)]
# calculation_multi(list_5, 0.1, 1, -350, len(list_5))

# list_6 = [(540, 80), (332, 40), (266, 47), (380, 44), (199, 38)]
# calculation_multi(list_6, 0.0001, 1, 1, len(list_6))

# x = 1,    y = 80
# x = 0.39, y = 40
# x = 0.2,  y = 47
# x = 0.53, y = 44
# x = 0,    y = 38
# list_7 = [(1, 80), (0.39, 40), (0.2, 47), (0.53, 44), (0, 38)]
# calculation_multi(list_7, 0.1, 1, 1, len(list_7))
