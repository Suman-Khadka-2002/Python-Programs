# while loop executes if the condition is true...

i =0
while (i<3): # here, the condition i(i.e. 0)<3, so executes
    print(i)
    i += 1

print("Done with the loop")

# normally, while loop is used for complex programs, such as user inputs: example

i = int(input("Enter a number: ")) # at first, initializing a value
while (i<=40):
    i = int(input("Enter a number: ")) # keeps on asking a number until a value greater than 40 is given
    print(i)

print("Done with the loop")

# Decrement loop AND while -else

count = 5   #initial value
while (count>0):    #executes till the condition remains true
    print(count)
    count -= 1
else:
    print("I am inside else")   # as soon as the loop finishes or skips or breaks, the else part is executed

# Emulte Do...while loop

while True:
    number = int(input("Enter a number: ")) # asks user for the input
    print(number)   #prints the number irrespective of the condition
    if not number > 0:
        break      #if the condition is true, the loop is exited, else the loop continues ...