import math

print("Lists")
x1 = [1, 2, 3]
x2 = ["A string", 2, 3.5, ["a list", "in a list"]]
print("x1: " + str(x1))
print("x2: " + str(x2))
print("x1[1:]: " + str(x1[1:]))   # from the second entry to the end
print("x2[0][2]: " + str(x2[0][2]))   # third character in the string in first list position
print("x2[-1][0]: " + str(x2[-1][0]))   # first item in the inner list in the last list position

print("### Change x1[0] to 5 ###")
x1[0] = 5

# list methods on pg 45
print("x1: " + str(x1))
x1.reverse()
print("Reverse x1: " + str(x1))
x1.append(4)
print("Append x1 with 4: " + str(x1))
y = x1.pop()   # pop removes a value and returns it. If no value is given, removes the last item
print("Pop method: ")
print("Popped item: " + str(y))
print("x1: " + str(x1))
x = list(range(5))
print("Range(5): " + str(x))
x = list(range(1, 4))
print("Range(1, 4): " + str(x))



print("\r\nTuples")
# like a list but can't change values
# instead of square brackets, use parenthesis
x = (1, 2, 3)
print("x[0]: " + str(x[0]))
print("x[:2]: " + str(x[:2]))

print("### Try Changing Values: ###")
try:
    x[0] = 4
    print("x: " + str(x))
except:
    print("Error changing values")
# assign multiple variables to one line with tuple packing
a, b = 4, 5
# LOOK AT NOTES
a, b = b, a
# any(x) - if any item in a list/tuple is true, it returns true
# all(x) - if all items in a list/tuple is true, it returns true

print("### Unpacking Works Like Regular Input ###")
sides = [3, 4]
print("math.hypot(3, 4): " + str(math.hypot(3, 4)))
print("sides: " + str(sides))
print("math.hypot(*sides): " + str(math.hypot(*sides)))