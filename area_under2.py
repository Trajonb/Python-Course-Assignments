#Area Under the Curve
#11/17/21

import math

def area_under_curve():

    a = int(input("Enter Starting Point(a): "))
    b = int(input("Enter End Point(b): "))
    n = int(input("Enter the Number of Rectangles(n): "))
    
    delta_x = (b-a)/(n)
    #print(delta_x)

    right_end = [1 + delta_x]
    left_end = [1]
    mid_point = []
    function_call = []
    individual_area = []
    total_area = 0 

    while len(left_end) < n:
        left_end.append(left_end[-1] + delta_x)

    #print(left_end)

    while len(right_end) < n:
        right_end.append(right_end[-1] + delta_x)

    #print(right_end)

    for i in range(0,n):
        first = left_end[i]
        #print(first)
        second = right_end[i]
        #print(second)
        mid = (first + second)/ (2)
        #print(mid)
        mid_point.append(mid)
    #print(mid_point)

    for i in mid_point:
        x = i
        #print(i)
        func = 1/x
        function_call.append(func)
        #print(func)

    #print(function_call)

    for i in function_call:
        total = i * delta_x
        #print(total)
        individual_area.append(total)


    for i in individual_area:
        total_area += i

    print(total_area)


    


area_under_curve()