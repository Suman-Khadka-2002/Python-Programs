# if-else statement--> evaluates the program if it is either true or false

a = int(input("Enter your age: "))
print("Your age is ", a)

# Conditonal Operators: <, >, >=, <=, ==, !=
print(a>18)  # returns true if the condition is true
print(a<=18)
print(a==18)
print(a!=18)
print()
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")

# elif statement---used for more than two conditions

num = int(input("Enter the value of num: "))

if(num<0):
    print("Number is negative")
elif(num == 0):
    print("Number is Zero")
elif(num == 999):
    print("Number is special")
else:
    print("Number is positive")

# Nested if-else statement---if-else inside if-else

num = 18
if (num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")