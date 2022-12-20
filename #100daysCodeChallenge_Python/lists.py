# lists are ordered collection of data items
# lists are changeable, i.e. we can alter them
# lists can contain any datatype's items (str, int, float, bool)

list1 = [3, 4, 5, "Messi"]
print(list1)
print(type(list1))

# we can access each items in the list by using their indexes as their orders are maintained...
print(list1[0]) # prints the first item i.e. 3
print(list1[3])
print(list1[-2])

# checking whether an item present in the list

if 5 in list1:  # checks '5' item in the list1
    print("Affirmative")
else:
    print("Negative")

if 'si' in "Messi":
    print("Affirmative!")

# to print whole items
print(list1[:])

# printing in the certain range
print(list1[1:3]) # inclueds item in index 1 to index 2 but ignores index 3 item

list2 = [3, 4, 5, "Messi", "Ronaldo", "Anime", 22, 20, 12, 3]
print(list2[1:9:3])


# List Comprehension : used for creating lists from other iterables like lists, tuples, dictionaries, sets and even from arrays and strings

nums = [i*i for i in range(5)] # prints the items upto range 5
print(nums)

num = [i*i for i in range(1, 10) if i%2==0]
print(num)

# accepts items with the small letter "o" in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_o = [name for name in names if "o" in name]
print(namesWith_o)

# accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
name_lenghty = [name for name in names if len(name)>4]
print(name_lenghty)