# HW3-3
# Alec Barker
# P2.4.6

num = 9

factorial = 1
factorial = 1

if num == 0:
    print()
elif num % 2 == 1:
    for i in range(1, num):
        if i % 2 == 1:
            factorial *= i
    print(factorial)
else:       
    for i in range(1, num + 1):
        if i % 2 == 0:
            factorial *= i
    print(factorial)