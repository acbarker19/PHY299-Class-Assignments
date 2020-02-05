a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

def binding_energy(A, Z):
    if A % 2 == 1:
        a5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a5 = 12
    elif A % 2 == 0 and Z % 2 == 1:
        a5 = -12
    
    B = (a1 * A) - (a2 * A**(2/3)) - (a3 * (Z**2 / A**(1/3))) - (a4 * ((A - 2 * Z)**2) / A) + (a5 / A**0.5)
    
    return B / A

print("Binding energy of A = 58 and Z = 28: ", binding_energy(58, 28))

def binding_energy_Z(Z):
    energy = []
    for A in range(Z, 3 * Z):
        energy.append(binding_energy(A, Z))
    return max(energy)

print("\r\nHighest Binding Energy for Z = 28: ", binding_energy_Z(28))

def binding_energy_100():
    energy = []
    for Z in range(1, 101):
        energy.append(binding_energy_Z(Z))
    return energy

print("\r\nFirst 100 Values for Z")
print("Highest value: ", max(binding_energy_100()))
print("Position of highest value: ", binding_energy_100().index(max(binding_energy_100())) + 1)
print("\r\nList of first 100 values: ", binding_energy_100())