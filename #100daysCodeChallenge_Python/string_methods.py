# Strings are immutable(cannot change)

a = 'Suman!!!!!!!!Suman'
print(len(a))
print(a.upper()) # prints whole in uppercase - creating new string 
print(a.lower())
print(a.rstrip("!")) # only strips trailing '!' ---for '!!Suman!!!'-> '!!Suman'
print(a.replace("Suman", "John")) # replaces the word Suman with John
print(a.split(" ")) # splits the string at specified instance and returns the separated strings as list items

title = "welcome to my world"
print(title.capitalize()) # capitalize the first letter 

str1 = "Welcome to the Console!"
print(str1.center(50)) # aligns the string to the center as per the paramerters by user

print(a.count('Suman')) # returns number of times the given value has occured

print(str1.endswith('!')) # returns bool value if condition satisfies
print(str1.endswith('to', 4, 10)) # does the letter at 4 to 10 index ends with 'to'

str2 = "he's name is Dan. He is an honest man."
print(str2. find("is")) # finds the index position where "is" is located
# print(str2.index("ishh")) # throws eror

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # returns boolean value if the string is alphanumeric
str1 = "welcome"
print(str1.islower()) # returns boolean value if the string is lowercase

str = "We wish you a Merry Christmas\n"
print(str)
print(str.isprintable()) # returns True if all given values are printable , if not, False

str3 = "   "
print(str3.isspace()) # returns True if the var contains space in it

str4 = "World Health Organization"
print(str4.istitle()) # returns true if the value is title like format (every word capitalize)
str5 = "To kill a mocking bird"
print(str5.istitle())

str = "Python is an Interpreted Language."
print(str.startswith("Python")) # returns true value is the str starts with the given name

str = "Python is an Interpreted Language."
print(str.swapcase()) # swaps uppercase letter to lower and viceversa

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # makes the data in title format-capitalize every word