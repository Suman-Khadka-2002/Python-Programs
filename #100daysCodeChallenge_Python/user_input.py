# input() is a python built-in function that takes input from the user.

a = input("Enter a name: ") # asks user to enter a name
print(a) #prints the name

# by default the input() gives string value.
# so we need to typecast the number to perform some operations

a = int(input("Enter 1st number: ")) #converts the input to integer datatype
b = int(input("Enter 2nd number: ")) #converts the input to integer datatype


# For int value all the operation works and gives output.
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

# for str value, only the concatenation operation

a = input("Enter a number: ")
b = input("Enter 2nd number: ")

print(a+b) # only gives output
print(a-b) # shows error
print(a*b) # shows error
print(a/b) # shows error
print(a//b) # shows error

# We can typecast this way as well:-

print(int(a) + int(b)) # addition operation is executed