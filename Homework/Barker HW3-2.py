# HW3-2
# Alec Barker
# P2.4.1

a = [1, 2, 3]
p = []

for num in a:
    product = 1
    for i in a:
        if i != num:
            product *= i
    p.append(product)

print(p)