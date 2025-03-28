import random as r
import matplotlib.pyplot as plt

N = 100000
left = set(range(N))
right = set()
left_size = [len(left)]
right_size = [len(right)]
largest_left = 0
smallest_right = N
largest = set()
smallest = 0
count = 0
stopping_value = 0
time = [0]

for i in range(N):
    par = r.randint(0, N - 1)
    
    if par in left:
        left.remove(par)
        right.add(par)
    else:
        right.remove(par)
        left.add(par)
    
    left_size.append(len(left))
    right_size.append(len(right))
    time.append(time[-1] + 1)
    
    if len(left) > largest_left:
        largest_left = len(left)
    if len(right) < smallest_right:
        smallest_right = len(right)
    
    count += 1
    
    if count % 100 == 0:
        largest.add(largest_left)
        smallest += smallest_right
        if abs(largest_left - smallest_right) < 0.05 * N \
        and stopping_value == 0:
            stopping_value = N / 2 + count
        largest_left = 0
        smallest_right = N
    if count == stopping_value and stopping_value != 0:
        break

plt.figure(dpi = 200)
plt.plot(time, left_size, c = 'r')
plt.plot(time, right_size, c = 'b')
plt.show()