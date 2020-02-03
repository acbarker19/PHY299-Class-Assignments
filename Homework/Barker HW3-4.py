# HW3-4
# Alec Barker
# P2.4.7 Part 1

# Fibonacci sequence
x = [1, 1]
y = [1, 1]
N = 500   # number of values
for i in range(N - 2):
    num = x[-2] + x[-1]
    x.append(num)
    y.append(int(str(num)[:1]))
    
actual_occurances = [y.count(1)/N, y.count(2)/N, y.count(3)/N, y.count(4)/N,
                     y.count(5)/N, y.count(6)/N, y.count(7)/N, y.count(8)/N,
                     y.count(9)/N]

expected_occurances = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

print("Expected Values of Benford's Law (1-10): ", expected_occurances)
print("\r\nActual Values of Benford's Law (1-10) for the Fibonacci Sequence: ", actual_occurances)