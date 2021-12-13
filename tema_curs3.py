#1
def my_function(*args):
    my_sum = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            my_sum = my_sum + i
    print(my_sum)

my_function(1, 5, -3)
my_function(3.4, -7.2)
my_function()
my_function(2, 4, 'abc')

#2
def my_function2(n):
    if n == 0:
        return 0
    return n + my_function2(n-1)

print(my_function2(5))

def my_function3(n):
    m = n-1
    if n==0:
        return 0
    if n % 2 == 0:
        return n+ my_function3(n-2)
    else:
        return m + my_function3(m-2)

print(my_function3(4))

def my_function4(n):
    m = n-1
    if n < 1:
        return 0
    if n % 2 != 0:
        return n + my_function4(n-2)
    else:
        return m + my_function4(m-2)

print(my_function4(5))

#3
def my_function5(n):
    if isinstance(n, int):
        print(n)
    else:
        print(0)

my_function5(0.5)
