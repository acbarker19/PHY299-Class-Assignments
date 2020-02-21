print("Exceptions and Debugging")
s1 = "4"
x1 = float(s1)
print("x1 =", x1)

"""
ValueError:
s2 = "Test Text"
x2 = float(x2)
print(x2)
"""

print()
try:
    y = 1 / 0
except ZeroDivisionError:
    print("1 can't be divided by 0")
print("Program keeps going no matter what happens.")
    
print()
x = 1
y = "Words"
try:
    if type(x) != int or type(y) != int:
        raise Exception("x and y must be integers")
except Exception as e:
    print(e)

print()
def demo(x):
    for i in range(5):
        print("i = {}, x = {}".format(i, x))
        x = x + 1
s = "an object"
demo(0)
demo(2)
demo(5)
print(s)