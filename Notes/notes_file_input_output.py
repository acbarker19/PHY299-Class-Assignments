import pickle

print("File Input/Output")

"""
file inside same directory:
    f = open("filename.txt")

file in a subfolder of python file:
    f = open("subfolder/filename.txt")
  
file in a parent or grandparent folder:
    f = open("../filename.txt")
    f = open("../../filename.txt")
    
file in a 'cousin' folder:
    f = open("../subfolder/filename.txt")

file in a specific path:
    f = open("C:/Users/username/subfolder/filename.txt")
    
    
    
to read/write to a file:
    f = open("filename.txt", argument)
    
arguments:
    r/rt  = read text (default)
    w/wt  = write text
    rb    = read binary
    wb    = write binary
"""

print("\r\nWriting Simple Text to File")
s1 = "text1"
s2 = "text2"
f = open("Data Files/sample text file.txt", "wt")
# if file doesn't exist, Python creates it
f.write(s1)
print(s2, file = f)
f.close()   # make sure to close file
print("Done")

print("\r\nWriting Number Data to File")
f = open("Data Files/sample text file.txt", "wt")
for i in range(1, 10001):
    print(i, i**2, i**3, i**4, sep = ", ", file = f)
    # sep creates a separater between files
    # printing to a file using print function
f.close()
print("Done")

print("\r\nReading and Printing Data from File")
f = open("Data Files/sample text file.txt", "rt")
for line in f:
    print(line, end = "")   # end = "" removes a new \n at the end
    if len(line) > 15:
        break
f.close()
print("Done")

print("\r\nReading and Manipulating Data from File")
f = open("Data Files/sample text file.txt", "rt")
for i, line in enumerate(f):
    if i == 4:                    # the 4th line for the values of 5
        s = line.split(",")       # now ["5", "25", etc]
        s = [int(j) for j in s]   # now [5, 25, etc]
        print(sum(s))
        break                     # stop loop when done
f.close()
print("Done")

print("\r\nReading and Writing Data as Binary")
x = [2, 4, 6, 8]
f = open("Data Files/test_list.txt", "wb")          # write binary
pickle.dump(x, f)                                   # object then file
f.close()
f = open("Data Files/test_list.txt", "rb")   # read binary
y = pickle.load(f)
f.close()
print(y)
print("Done")

print("\r\nP2.6.1")
tallest_name = "N/A"
tallest_num = 0
widest_name = "N/A"
widest_num = 0
f = open("Data Files/redwood-data.txt", "rt")
for i, line in enumerate(f):
    if line.startswith("#") == False:
        tree = line.split("\t")
        height = float(tree[3].replace("\n", ""))
        width = float(tree[2])
        if height > tallest_num:
            tallest_num = height
            tallest_name = tree[0]
        if width > widest_num:
            widest_num = width
            widest_name = tree[0]     
f.close()
print("Tallest Tree: {0}\tHeight: {1}".format(tallest_name, tallest_num))
print("Widest Tree: {0}\tWidth: {1}".format(widest_name, widest_num))
print("Done")