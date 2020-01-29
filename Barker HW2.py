# HW 2
# Alec Barker

print("Q2.3.4")
"""
Output:
1st
3rd
5th

The print statement has two values that are formatted to take in the two
variables. The first formatted value is the number n, and the second formatted
value is a piece of the string suff. The string contains all the suffixes for
numbered positions. The second formatted value is a list that is a slice of the
string. It takes the characters between the n position * 2 (since there are two
letters per suffix) and two spaces after (again, because there are two letters
per suffix).
"""

suff = 'thstndrdththththththth'
n = 1
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))
n = 3
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))
n = 5
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))



print("\r\nP2.3.3")
a11 = 1.0
a12 = 5.3
a13 = -0.4
a21 = -9.1
a22 = 0.0
a23 = 7.3
a31 = -2.9
a32 = -8.1
a33 = -6.8
top_row_list = [a11, a12, a13]
middle_row_list = [a21, a22, a23]
bottom_row_list = [a31, a32, a33]

top_row = ""
middle_row = ""
bottom_row = ""

for i in range(0, 3):
    if(i == 0):
        top_row += "["
        middle_row += "["
        bottom_row += "["
        
    if top_row_list[i] < 0:
        top_row += " " + str(top_row_list[i])
    else:
        top_row += "  " + str(top_row_list[i])
    
    if middle_row_list[i] < 0:
        middle_row += " " + str(middle_row_list[i])
    else:
        middle_row += "  " + str(middle_row_list[i])
        
    if bottom_row_list[i] < 0:
        bottom_row += " " + str(bottom_row_list[i])
    else:
        bottom_row += "  " + str(bottom_row_list[i])
        
    if(i == 2):
        top_row += " ]\r\n"
        middle_row += " ]\r\n"
        bottom_row += " ]\r\n"

s_a = top_row + middle_row + bottom_row

print(s_a)

a11 = 1
a12 = 1
a13 = 0
a21 = 0
a22 = 0
a23 = 0
a31 = 1
a32 = 0
a33 = 1

top_row_list = [a11, a12, a13]
middle_row_list = [a21, a22, a23]
bottom_row_list = [a31, a32, a33]

top_row = ""
middle_row = ""
bottom_row = ""

for i in range(0, 3):
    if(i == 0):
        top_row += "["
        middle_row += "["
        bottom_row += "["
    
    top_row += " " + str(top_row_list[i])
    middle_row += " " + str(middle_row_list[i])
    bottom_row += " " + str(bottom_row_list[i])
    
    if(i == 2):
        top_row += " ]\r\n"
        middle_row += " ]\r\n"
        bottom_row += " ]\r\n"

s_b = top_row + middle_row + bottom_row

print(s_b)