# HW 8-2
# Alec Barker

import math

def provide_P(n):
    P = [1, 1, 1]
    
    for i in range(3, n):
        P.append(P[i - 2] + P[i - 3])
    
    return P
        
def provide_Q(n):
    Q = [3, 0, 2]
    
    for i in range(3, n):
        Q.append(Q[i - 2] + Q[i - 3])
    
    return Q

def prime_num_list(n):
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
    
    return prime_nums

n = 10000

P = set(provide_P(n))
Q = set(provide_Q(n))

print("a. Unique Values in P:", len(P))
print("a. Unique Values in Q:", len(Q))
      
print("b. Total Unique Values of P and Q:", len(P) + len(Q))

prime_nums = set(prime_num_list(n))
print("c. Prime Values in P:", len(P.intersection(prime_nums)))
print("c. Prime Values in Q:", len(Q.intersection(prime_nums)))

print("d. Shared Non-Prime Value:",
      *P.intersection(Q) - prime_nums)