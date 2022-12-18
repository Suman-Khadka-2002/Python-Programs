# Functions is a block of code that performs a specific task whenever it is called.

# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print(gmean)

# c = 8
# d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)

#  you can do this using function:

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print (mean)

def isGreater(a, b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greaer or equal")

def isLesser(a, b):
    pass  # move ahead of this function to run code i.e. pass

a = 9   # value initialization
b = 8
isGreater(a, b) # calls isGreater function
calculateGmean(a, b)    # calls calculateGmean function