# anything you include inside single/double quote(' '/" ") is an string.

name = "Suman"
friend = 'Roberto'
print("hello "+ friend)

# We can use escape sequence or double-single quote to include quotes inside a sentence
text = "this is a 'sentence'"
text = "this is also a \'sentence\'"
print(text)

# multiple line string can be used using triple quote- ''' '''/""" """
greet = """
Hi,
Good morning!"""
print(greet)

# sting is "like a" array of characters which can shown with following properties:
name = 'apple'
print(name[0]) # prints the character in the 0 index of the name value
print(name[4])
print(name[0:3]) #prints the characters from range of index 0 to 2 as index 3 is not included
# print(name[5]) # throws an error as the index 5 is not present

# using a for loop

for character in name: #character is varibale that prints character scanning one-by-one from'apple' in name turn-wise
    print(character)