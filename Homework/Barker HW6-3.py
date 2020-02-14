# HW 6-3
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

def find_value(file, column, row):
    try:
        f = open(file, "rt")
        
        columns_found = False
        answer_found = False
        
        for line in f:
            if answer_found:
                break
            if line.startswith("#") == False:
                if columns_found == False:
                    columns = get_all_values(line.lower())
                    columns_found = True
                elif line.lower().startswith(row.lower()):
                    data = get_all_values(line.lower())
                    for i in range(len(columns)):
                        if columns[i].startswith(column.lower()):
                            row_answer = get_row_title(line.lower())
                            column_answer = columns[i]
                            answer = data[i + 1]
                            answer_found = True
                            break
        
        print("Query: {}\r\nPlanet: {}\r\nAnswer: {}\r\n".format(row_answer.title(),
              column_answer.title(),
              answer.title()))
        
        f.close()
    except FileNotFoundError:
        print("File could not be found")

find_value("Data Files/planetary-fact-sheet.txt", "Mars", "Orbital Velocity")
find_value("Data Files/planetary-fact-sheet.txt", "Nept", "Mean Temp")
find_value("Data Files/planetary-fact-sheet.txt", "j", "n")