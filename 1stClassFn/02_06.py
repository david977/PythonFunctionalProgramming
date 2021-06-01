#Higher Order Function

def divide(x,y):
    # if y == 0:
        # print('Warning: Someone is trying to divide by zero')
        # return
    return x/y

def second_argument_isnt_zero(func):
    def safe_version(*args): # get all the arguments that we pass in
        if args[1]==0:
            print('Warning: second argument is 0')
            return
        return func(*args) #Pass all the arguments otherwise

    return safe_version

divide_safe = second_argument_isnt_zero(divide)

print(divide_safe(10,2))