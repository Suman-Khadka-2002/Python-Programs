l = [1, 2, 8, 12, 4, 6, 2, 2]
print(l)

# l.append(7)    # adds 7 in the list
# l.sort()    # sorts in ascending order
# l.sort(reverse=True)   #sorts in descending order
# l.reverse()   # reverses the items in the list
# print(l.index(2))     #prints the index of the item
# print(l.count(2))    #counts the item in list

# new_l = l   # Don't do this
# new_l[0] = 22       #changes the content in the orignal var too

# new_l = l.copy()
# new_l[0] = 22       #copies the list and edited is stored in the new list

# l.insert(1, 999)        #store 999 in index 1

new_l1 = [900, 1000, 1100]
# l.extend(new_l1) # extend the list l merging new_l1 to the end, which changes the list l
#     # but if you don't want to change the original list, you concatenate which creates a new list

m = l + new_l1      # concatenates two lists which creates a new list
print(m)

print(l)

