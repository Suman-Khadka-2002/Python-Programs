# # Day 21 of 100DaysCodeChallenge

# def average(a=9, b=1):
#     print("The average is : ", (a+b)/2)

# average() # runs using the default arguments in the function
# # average(4, 6) # these are the required arguments

# def name(fname, mname = "Jhon", lname = "Whatson"): # here, fname -> required arg, mname -> default arg
#     print("Hello, ", fname, mname, lname)

# name("Amy", mname="Jane") # here, mname-> keyword arg

#  variable length arguments:

def average(*numbers): # here we get input as tuples
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("The average is : ", sum/len(numbers))
    return sum / len(numbers)   # returns the value back to the calling function

# average(5, 7)
c = average(4, 8) # c stores the value from average calculations
print(c)

# if you want input as a dictionary

# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James") # here, input as key-value pairs are given