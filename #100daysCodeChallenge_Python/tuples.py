# Tuples are ordered collection of data items.
# Tuples are unchangeable : we cannot alter them

# tup = (1) # comma must be included otherwise python will show int datatype
# tup = (1, ) # shows tuple as datatype
tup = (1, 2, 123, 234, 34, "red")
# tup[0] = 1000 # cannot change data in tuple , and shows error
# print(type(tup))
print(tup)
print(tup[2]) # prins the item in index 2
print(tup[-3]) #len(tup)-3
print(tup[1:6:2])

if "red" in tup:
    print("Affirmative")

tup2 = tup[1: 3] #creates new tuple
print(tup2)