import math

print("If/Elif/Else Statements")
name = 12243
# name = "John"
# name = False
if type(name) == str:
    print("Your name is {0}".format(name))
elif type(name) == bool:
    print("Your name can't be a Boolean")
else:
    print("Your name must be a String")
    
print("\r\nDetermining Position on a Number Line")
for x in range(10):
    if x <= 3:
        print(x, " is less than or equal to 3")
    elif x > 5:
        print(x, " is greater than 5")
    else:
        print(x, " is 4 or 5")
        
print("\r\nSum of Even and Sum of Odd Numbers")
N = 100
even = 0
odd = 0
for i in range(N):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("Even Sum: ", even)
print("Odd Sum: ", odd)



print("\r\nWhile Loop")
i = 0
while i < 10:
    print("i = ", i)
    i += 1
else:
    print("The last value was ", i)
    
print("\r\nE2.22: Euclid's Algorithm")
a, b = 1071, 462
while b:
    # b is True while > 0
    print("a = {0:4}\tb = {1:4}\ta % b = {2:4}".format(a, b, a % b))
    # {0:4} in the above will limit the length of the string to 4
    a, b = b, a % b
print("Greatest common divisor = ", a)

print("\r\nP2.5.2")
H = 0
c = 0.01
Ka = 1.78e-5
TOL = 1e-10
dPH = 1
counter = 0
while dPH > TOL:
    Hp = math.sqrt(Ka * (c - H))
    dPH = Hp - H
    H = Hp
    counter += 1
    if counter > 100:
        break
print("PH: {0:.2f}".format(-math.log(H, 10)))



print("\r\nBreak Command")
# Ends loop
i = 0
while True:
    i += 1
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")
    if i >= 10:
        break
    
print("\r\nPass Command")
# Skips over a section
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i, " is odd")
        
print("\r\nContinue Command")
# Ends current iteration and moves onto next
for i in range(10):
    if i % 2 == 0:
        continue
    else:
        print(i, " is odd")
        
        
    
print("\r\nQ2.5.1")
a = [2, 4, 10, 6, 8, 4]
low = min(a)
high = max(a)
out = []
for i in a:
    out.append((i - low) / (high - low))
print(out)