# # Tuples are immutable, hence to add, remove or change tuple items, then first you must convert the tuple to a list then, perform the operations

# # Example 1
# countries = ("Spain", "Italy", "India", "Nepal", "Argentina")
# temp = list(countries)
# temp.append("Bangladesh") # add item
# temp.pop(3) # removes item from index 3
# temp[2] = "Switzerland" # changes the item in index 2
# countries = tuple(temp)
# print(countries)

# Example 2
tuple1 = (0, 1, 2, 3, 2, 3, 1 ,3, 2)
# result = tuple1.count(3) #counts the item in the tuple
result = tuple1.index(1) # finds the index of 1 in the tuple
result = tuple1.index(3, 4, 8) # finds the index of 3 in the range of start:4 to end: 8 
result = len(tuple1) # prints the length of the tuple
print("Count of 3 in tuple1 is : ", result)