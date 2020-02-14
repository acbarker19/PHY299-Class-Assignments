# HW 6-1
# Alec Barker

# Q2.7.3

def digit_sum(n):
    """ Find the sum of the digits of integer n. """
    s_digits = list(str(n))
    dsum = 0
    for s_digit in s_digits:
        dsum += int(s_digit)
    return dsum
        
def is_harshad(n):
    return not n % digit_sum(n)

print(is_harshad(21))