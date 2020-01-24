print("Strings")
print("'abc''cdf' = " + 'abc''cdf')
print("'abc' + 'cdf' = " + 'abc' + 'cdf')
print("'abc' * 3 = " + 'abc' * 3)
print("str(4*2) = " + str(4*2))
print('Quotes within quotes: I said to her, "but why is the tomato blue?"')



"""
\t   tab
\n   new line
\r   carriage return
\'   single quote
\"   double quote
"""



print("\r\nBackslash Commands")
print("a\\tbcd\\nefg\\\"hij\\' = a\tbcd\nefg\"hij\'")



# can use triple quotes to print strings on multiple lines
print("\r\nasy Strings Across Multiple Lines")
text = """Test
Message
with
Triple
Double
Quotes"""
print(text)



print("\r\nSlicing and Indexing")
s = "abcdefg"
print("s = " + s)
print("s[0]: " + s[0])
print("s[3]: " + s[3])
print("s[-1]: " + s[-1])
print("s[1:4]: " + s[1:4])
print("s[0:6:2]: " + s[0:6:2])
print("s[::-1]: " + s[::-1])

print("\r\nSlicing and Indexing Example")
s = "I'm a little teapot"
print(s)
print(s[:12])
print(s[-3:] + s[:5])
print(s[:-7:-1])
print(s.replace("little", "big"))



print("\r\nSwitching to Uppercase and Stripping a String")
s = "+-a line from a text fileGGG"
# strip removes characters from the beginning and end until it reaches a character not in parenthesis
s2 = s.strip("+-G")
s2 = s2.title()
s2 = s2.replace("A Line", "An Awesome Line")
print("s = " + s)
print("s with stripping, title, and replace commands = " + s2)



print("\r\nInsert Data into a String")
person = "Mrs. White"
place = "kitchen"
weapon = "knife"
sentence = "The murder was done by {0} in the {1} with the {2}.".format(person, place, weapon)
print(sentence)

# {0:.3f} includes 3 digits after the decimal in the 0th place of the string
# {0:.2g} includes 2 digits total
# {0:.2E} includes 2 digits after the decimal and switches the rest to exponential format
score = 5.6789
sentence = "The restaraunt had a rating of {0:.3f}".format(score)
print(sentence)
sentence = "The restaraunt had a rating of {0:.2g}".format(score)
print(sentence)
sentence = "The restaraunt had a rating of {0:.2E}".format(score)
print(sentence)



print("\r\nQ2.3.2 - Is a String a Palindrome?")
word = "racecar"
print("Is " + word + " a palindrome?")
print(word[::-1] == word)
word = "hello"
print("Is " + word + " a palindrome?")
print(word[::-1] == word)



print("\r\nP2.3.1 - Is a Nucleotide Sequence a Palindrome with its Pair?")
s = "TGGATCCA"
# replace nucleotide with pair
s2 = s.replace("T", "a")
s2 = s2.replace("A", "t")
s2 = s2.replace("C", "g")
s2 = s2.replace("G", "c")
# return all to uppercase
s2 = s2.upper()
print("Is " + s + "'s pair a palindrome to the original?")
print(s[::-1] == s2)