# HW 8-1
# Alec Barker

def get_all_values(text):
    values = []
    
    while True:
        if text != "\n" and text != "" and text != "n":
            if "\t" in text:
                index = text.find("\t")
                values.append(text[:index].strip())
                text = text[index:]
                text = text.lstrip()
            else:
                values.append(text.strip())
                break
        else:
            break
        
    return values

def get_row_title(text):
    index = text.find("\t")
    value = text[:index].strip()
    return value

def get_data_from(file):
    D = {}
    
    try:
        f = open(file, "rt")
        
        columns_found = False
        
        for line in f:
            if line.startswith("#") == False:
                if columns_found == False:
                    columns = get_all_values(line)
                    
                    for column in columns:
                        D[column] = {}
                    
                    columns_found = True
                else:
                    row_data = get_all_values(line)
                    for i, key in enumerate(D):
                        D[key][row_data[0]] = row_data[i + 1]
        f.close()
        
        return D
    except FileNotFoundError:
        print("File could not be found")

D = get_data_from("Data Files/planetary-fact-sheet.txt")

print("All data about Mars:")
for key in D["MARS"]:
    print("{}: {}".format(key, D["MARS"][key]))

print()
print("Does Mars have a ring system?", D['MARS']['Ring System?'])