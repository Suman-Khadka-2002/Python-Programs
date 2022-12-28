# Comments some part to run specific part of code
# string formatting is done in python using format method.

# letter = "Hey My name is {} and I am from {}"
letter = "Hey My name is {1} and I am from {0}" # uses the index of the arguments

country = "Nepal"
name = "Suman"

print(letter.format(country, name))

# using fstrings, it becomes more easier:
print(f"Hey My name is {name} and I am from {country}")
print(f"to print as it is: Hey My name is {{name}} and I am from {{country}}")

# for decimal values, you can use .2f for 2 digits after .
price = 69.0999999
bill = f"The total is {price:.2f} dollars!"
print(bill)

print(f"{2 * 20}") # this will return str type value i.e. 40 is a string
print(type(f"{2 * 20}"))