#Returning Functions

def create_printer():
    def printer():
        print('Hello Functional!')
    return printer

my_printer = create_printer()
my_printer()

# def double(x):
#     return x*2

# def treble(x):
#     return x*3
#
# def quadruple(x):
#     return x*4

def create_multiplier(a):
    def multiplier(x):
        return x*a
    return multiplier

double = create_multiplier(2)
treble = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(treble(6))
print(quadruple(7))