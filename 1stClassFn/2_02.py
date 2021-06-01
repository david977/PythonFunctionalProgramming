#Function as data part 2
import math

def double(x):
    return x*2

def minus_one(x):
    return x-1

def squared(x):
    return x*x

function_list = [
    squared,
    double,
    minus_one,
    math.sqrt

]

my_number = 3

# my_number = double(my_number)
# my_number = minus_one(my_number)
# my_number = squared(my_number)

for func in function_list:
    my_number = func(my_number)

print(my_number)