print("Dictionaries")
fav_colors = {"Elise" : "purple", "Sean" : "Red"}
print("fav_colors['Elise'] =", fav_colors["Elise"])

print("\r\nList of Colors and Tokens")
colors = ["red", "blue", "yellow"]
tokens = [False, False, False]
print("Colors =", colors)
print("Tokens =", tokens)
tokens[colors.index("blue")] = True
print("Tokens After tokens[colors.index('blue')] = True =", tokens)
print("### Switch Tokens to Dictionary ###")
tokens = {}
for c in colors:
    tokens[c] = False
print("Tokens =", tokens)
tokens["red"] = True
print("Tokens After tokens['red'] = True =", tokens)
print("Keys =", list(tokens.keys()))
print("Values =", list(tokens.values()))

s = "abbccd" * 30
letters = {"a" : s.count("a"), "b": s.count("b"), "c" : s.count("c"),
           "d" : s.count("d"), "e" : s.count("e")}
print("\r\nCounting characters in '{}' = {}".format(s, letters))



# sets are unordered lists of unique items
print("\r\nSets")
x = [1, 1, 2, 2, 3, 4]
print("x =", x)
print("set(x) =", set(x))

# common set methods
s = {1, 1, 2, 2, 3, 4}
s.add(6)       # add an item
s.remove(1)    # remove an item or get error if item is not in set
s.discard(2)   # remove an item with no error if item is not in set
s.pop()        # remove and return random item

a = {1, 2, 3}
b = {3, 4, 5}
print("\r\na =", a)
print("\r\nb =", b)
print("a < b =", a < b)
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("a - b =", a - b)
print("b - a =", b - a)

s = "aaaaaahhhhh"
print("s =", s)
print("set(s) =", set(s))
print("Is s a pangram (contains every letter of the alphabet?",
                       len(set([x for x in s if x.isalpha()])) == 26)