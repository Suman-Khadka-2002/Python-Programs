# for loops can iterate over a sequence of iterable objects
name = 'Christopher'
for i in name:
    print(i)    #prints each charcter to the length of the name

colors = ['Red', 'Green', 'Blue', 'Yellow']
for color in colors:
    print(color)
    
# range() : for a certain limit
for k in range(5):
    print(k+1)   #starts from 1 index instead of 0

for k in range(1, 4):
    print(k)    # prints from 1 to 3 excluding 4

for k in range(1, 12, 2):
    print(k)    #prints with step 2 ahead which is 1, 3, 5, 7, 9, 11 in this case

