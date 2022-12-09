# Iterator 

iter_list=iter(['coding', 'is', 'fun'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

# Generator is a function that returns an object(iterator) which we can iterate over (one value at a time)
# Generator is another way of creating iterators in a simple way where it uses the keyword "yield" instead of returning it in a defined function. For example:

def sq_numbers(n):
    for i in range (1, n+1):
        yield i*i

a = sq_numbers(3)
print("the sq of numbers 1 2 3 are : ")
print(next(a))
print(next(a))
print(next(a))

# using for loop
for a in sq_numbers(3):
    print(a)


#shorter version for generator
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = (num for num in num_list if num%2==0)
print(next(new_list)) # 2   
print(next(new_list)) # 4