import math

def add(x):
    sum = 0
    for num in x:
        sum += num
    return sum

def sub(x, y):
    sum = x
    for num in x:
        sum -= num
    return sum

def mult(x):
    result = 1
    for num in x:
        result *= num
    return result

def div(x, y):
    result = x
    for num in y:
        result /= num
    return result