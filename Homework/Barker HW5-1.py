# HW 5-1
# Alec Barker

# P2.6.3

def get_next_value(text):
    index = text.find('  ')
    text = text[index:]
    text = text.lstrip()
    index = text.find('  ')
    new_value = text[:index]
    
    try:
        new_value = float(new_value)
    except:
        pass
        
    return text, new_value

def get_esi(value, earth_value, weight):
    esi = (1 - abs((value - earth_value) / (value + earth_value)))**(weight / n)
    return esi

f = open("Data Files/ex2-6-g-esi-data.txt", "rt")

n = 4
earth_radius = 0
earth_density = 0
earth_v_esc = 0
earth_Tsurf = 0
closest = ["", 0]

for i, line in enumerate(f):
    if i > 2:
        text, name = get_next_value(line)
        text, mass = get_next_value(text)
        text, radius = get_next_value(text)
        text, density = get_next_value(text)
        text, g = get_next_value(text)
        text, v_esc = get_next_value(text)
        text, a = get_next_value(text)
        text, Tsurf = get_next_value(text)
        text, Teq = get_next_value(text)
        
        if name == "Earth":
            earth_radius = radius
            earth_density = density
            earth_v_esc = v_esc
            earth_Tsurf = Tsurf
        else:
            esi_radius = get_esi(radius, earth_radius, 0.57)
            esi_density = get_esi(density, earth_density, 1.07)
            esi_v_esc = get_esi(v_esc, earth_v_esc, 0.7)
            esi_Tsurf = get_esi(Tsurf, earth_Tsurf, 5.58)
            
            product = esi_radius * \
                    esi_density * \
                    esi_v_esc * \
                    esi_Tsurf
            product = round(product, 4)
            
            if product > closest[1]:
                closest = [name, product]
            
            print("{}'s ESI value: {}".format(name, product))

print()
print("The most similar planet to Earth is {} with an ESI value of {}".format(
        closest[0], closest[1]))

f.close()