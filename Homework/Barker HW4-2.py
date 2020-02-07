# HW 4-2
# Alec Barker

import math

# P2.5.8

n = 10000
p = 2
prime_nums = list(range(1, n + 1))

while p <= n / 2:
    for m in range(2, math.ceil(n / p) + 1):
            try:
                prime_nums.remove(m * p)
            except:
                pass
    
    for num in prime_nums:     
        if num > p:
            p = num
            break

print(prime_nums)