import math

x = 2   # normal integer
y = 3.4E-2   # 3.4 * 10^-2
z = complex(3, 4)   # complex(<real>, <imaginary>)



print("Division")
print("5.0 / 2.0 = " + str(5.0 / 2.0))
print("5.0 // 2.0 = " + str(5.0 // 2.0))   # integer division
print("5.0 % 2.0 = " + str(5.0 % 2.0))   # modulus (remainder)



"""
Order of operations

**   exponent first
*, /, //, %   multiplication and division next
+, -   addition and subtraction last

"""



print("\r\nExponents")
print("9/3*2 = " + str(9/3*2))
print("9*3/2 = " + str(9*3/2))
print("9**2**2 = " + str(9**2**2))
print("3**(2**2) = " + str(3**(2**2)))
print("(3**2)**2 = " + str((3**2)**2))



print("\r\nAbsolute Value")
print("abs(-2.5) = " + str(abs(-2.5)))
print("abs(2.5) = " + str(abs(2.5)))
print("abs(4+3j) = " + str(abs(4+3j)))   # length of a vector with coordinates (4, 3)
print("round(3.5) = " + str(round(3.5)))
print("round(4.5) = " + str(round(4.5)))
# the 2 rounded numbers are equal because .5 will sometimes round up and sometimes round down



print("\r\nMath Functions")
print("math.cos(2*math.pi) = " + str(math.cos(2*math.pi)))   # cos(2pi)
print("math.sin(math.radians(32.8)) = " + str(math.sin(math.radians(32.8))))   # sin(32.8 degrees) -> must convert inside from degrees to radians
print("math.pi**math.pi = " + str(math.pi**math.pi))   # pi^pi
print("math.factorial(9) = " + str(math.factorial(9)))   # 9!
print("math.hypot(2.5, 8.42) = " + str(math.hypot(2.5, 8.42)))   # hypotenuse of right triangle with side of length 2.5 and 8.42



print("\r\nExample E2.3")
a = 3
b = 4
c = 5
s = 0.5 * (a + b + c)
A = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("math.sqrt(s * (s - a) * (s - b) * (s - c)) = " + str(A))



print("\r\nLocation in Memory and Assigning Variables to Other Variables")
d = 12
e = d
print("d = " + str(d))
print("e = " + str(e))
print("e = d")
print("memory location of d = " + str(id(d)))
print("memory location of e = " + str(id(e)))
d = 8
print("### Change D to 8 ###")
print("d = " + str(d))
print("e = " + str(e))
print("memory location of d = " + str(id(d)))
print("memory location of e = " + str(id(e)))



print("\r\nLocation in Memory and Variables with Same Values")
d = 1200
e = 1200
print("d = " + str(d))
print("e = " + str(e))
print("memory location of d = " + str(id(d)))
print("memory location of e = " + str(id(e)))
print("d == e = " + str(d == e))   # == compares if the values are the same
print("d is e = " + str(d is e))   # is compares if the objects are the same
d = 8
print("### Change D to 8 ###")
print("d = " + str(d))
print("e = " + str(e))
print("memory location of d = " + str(id(d)))
print("memory location of e = " + str(id(e)))
print("d == e = " + str(d == e))
print("d is e = " + str(d is e))



print("\r\nExample Comparison")
print("2.4**2.6 > 2.6**2.4 = " + str(2.4**2.6 > 2.6**2.4))



print("\r\nExample with Precise Comparison")
d = 0.1**2   # problem
e = 0.01   # expected answer
print("d = " + str(d))
print("e = " + str(e))
print("d == e = " + str(d == e))