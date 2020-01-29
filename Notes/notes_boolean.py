print("Booleans")
P = True
Q = False
R = True
print("P and Q: " + str(P and Q))
print("P or Q: " + str(P or Q))
print("not P or Q: " + str(not P or Q))



print("\r\nBoolean Launch Code Example")
# the president must be available and 2 of the 3 officers must be available to launch the missile
pres = True
off_1 = True
off_2 = True
off_3 = False
print("Can Launch Missile: " + str(pres and ((off_1 and off_2) or (off_1 and off_3) or (off_2 and off_3))))
# can also use integers
pres = 1
off_1 = 1
off_2 = 1
off_3 = 0
print("Can Launch Missile: " + str(pres and (off_1 + off_2 + off_3) >= 2))



print("\r\nQ2.2.3")
print("a. 9 + 6j/2 = " + str(9 + 6j/2))
print("b. complex(4,5).conjugate().imag = " + str(complex(4,5).conjugate().imag))
print("c. complex(0, 3j) = " + str(complex(0, 3j)))
print("d. round(2.5) = " + str(round(2.5)))
print("e. round(-2.5) = " + str(round(-2.5)))
print("f. abs(complex(5, -4)) == math.hypot(4,5) = " + str(abs(complex(5, -4)) == math.hypot(4,5)))