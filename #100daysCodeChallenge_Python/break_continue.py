# # break statement enables a program to skip over a part of the code and terminates the very loop it lies within

# # multiplicaiton
# for i in range(12):
#     if (i == 10):   #as soon as i = 10 , the program exits the loop
#         break
#     print("5 x ", i+1, "=", 5 * (i+1))

# print("The loop is exited")

# continue -- skips the iteration
for i in range(12):
    if(i == 10):
        print("skip the iteration")
        continue
    print("5 x ", i+1, "=", 5 * (i+1))