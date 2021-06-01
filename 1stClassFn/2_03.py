#Passing Functions as arguments.

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def combine_2_3(func):
    return func(2,3)

print(combine_2_3(min))

def combine_names(func):
    return func('Prashant','Mahato')

def append_with_space(str1,str2):
    return f'{str1} {str2}'

def get_government_form_notation(first,last):
    return f'{last.upper()},{first.upper()}'

print(combine_names(get_government_form_notation))