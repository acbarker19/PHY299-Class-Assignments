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

print("\r\nZip() Function for Lists")
# zip(x, y) combines list x with list y
scores = [90, 70, 100]
names = ["Alice", "Jack", "Charlie"]
print("scores = " + str(scores))
print("names = " + str(names))
z = list(zip(scores, names))
print("Zipped List = " + str(z))
print("Sorted List = " + str(sorted(z)))

print("### Unzip the Sorted List ###")
sorted_scores, sorted_names = zip(*z)
# to unzip, use zip(*zipped_list)
print("sorted_scores = " + str(sorted_scores))
print("sorted_names = " + str(sorted_names))



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



print("\r\nFor Loops")
x = [5, 2, 1, 4, 7]
total = 0
print("for i in x:")
for i in x:
    print(i)
    total += i
print("total = {0}".format(total))

x = ["apple", "orange", "pineapple"]
print("for i in range(len(x)):")
for i in range(len(x)):
    print(x[i])

print("for i, entry in enumerate(x):")
for i, entry in enumerate(x):
    # enumerate() provides two iterators
    print(i, ":", entry)
    
x = [0, 1, 2, 3, 4, 5]
print("x = " + str(x))
print("[i**2 for i in x]")
y = [i**2 for i in x]
print("y = " + str(y))

print("\r\nFibonacci Sequence Example")
x = [1, 1]
N = 10   # number of values
for i in range(N - 2):
    x.append(x[-2] + x[-1])
print(x)

print("\r\nSum of All Numbers 1-100 Example")
print("sum([math.sqrt(i) for i in range(1, 101)]) = " + str(sum([math.sqrt(i) for i in range(1, 101)])))

print("\r\nNested For Loops")
x = [1, 2, 3]
y = ["apple", "applesauce", "apple juice"]
for i in x:
    for j in y:
        print(i, j)
    print("finished the inner loop for {0}".format(i))
    
print("\r\nNested For Loop Example")
x = ["FBI", "CIA", "NBA", "NFL", "MLB"]
for acronym in x:
    edited = ""
    for letter in acronym:
        edited += letter + "."
    print(edited)
    
print("\r\nQ2.4.4: Digits of Pi Example")
odd = 1
my_pi = 0
for i in range(19):
    my_pi += math.sqrt(12) * (-1)**i * (1 / (3**i * odd))
    odd += 2
print("First 20 digits of pi: " + str(my_pi))