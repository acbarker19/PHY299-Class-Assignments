print("Functions")
def sample_function1():
    print("sample_function1 called")
sample_function1()

def sample_function2(a, b):
    return a**b
y = sample_function2(3, 4)
print("sample_function(3, 4): ", y)



def hypot(x, y):
    """Determines the hypotenuse of a right triandle with the given sides."""
    return (x**2 + y**2)**0.5
h = hypot(3, 4)
print("\r\nhypot(3, 4): ", h)
print("Doc String for hypot(x, y): ", hypot.__doc__)



print("\r\nSum of Numbers Outside the Function")
def f():
    print("Sum of {0}: {1}".format(a, sum(a)))

a = list(range(5))
f()
a = list(range(10))
f()



print("\r\nPlugging Values into a Function")
def f(a = 1, b = 2, c = 3):
    print(a, b, c)
# takes in arguments in order of appearance
f(1, 2, 3)
f(3, 2, 1)
# explicitly filling the arguments allows you to change the order
f(a = 1, b = 2, c = 3)
f(c = 3, a = 1, b = 2)
# not calling an argument will use default value
f(b = 2, c = 3)
# can mix for positional then keyword
f(5, b = 2, c = 4)
# CAN'T mix keyword then positional
# f(b = 2, 5, 6)



print("\r\nGlobal vs Local Function Variables")
def f():
    a = 5
    print(a, b)
    
b = 6
# functions look in local then global
print("Example 1: ", f())
# global variables may be overwritten by local variables
a = 8
print("Example 2: ", f())

def f(a):
    a += 1
    print("In function: ", a)
a = 5
f(a)
print("End of global: ", a)



print("\r\nChanging Global Variable Inside of Function")
def f():
    global x   # the function knows that x is globally defined
    x += 1
    print("In function: ", x)
x = 5
f()
f()
f()
print("End of global: ", x)



print("\r\nChanging Global Variable Outside of Function")
def f(a):
    print(a + 1)
    return a + 1
x = 5
x = f(x)
x = f(x)
x = f(x)



print("\r\nDetermine Balance over Time with Interest")
balance = 100
def add_interest(balance, rate):
    balance += balance * rate / 100
    return balance
for year in range(4):
    balance = add_interest(balance, 5)
    print("Balance after year {0}: ${1:.2f}".format(year + 1, balance))



print("\r\nX to the X Power to the X Power ... for N Number of Times")
x = 5
n = 3
def f(orig_x, x, orig_n, n):
    x = orig_x**x
    n -= 1
    if n > 1:
        f(orig_x, x, orig_n, n)
    elif n == 1:
        print("Value of {0}, {1}: {2}".format(orig_x, orig_n, x))
        print("Length of {0}, {1}: {2}".format(orig_x, orig_n, len(str(x))))
f(x, x, n, n)