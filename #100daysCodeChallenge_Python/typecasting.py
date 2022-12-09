# Two types of typecasting: Explicit typecasting and Implicit typecasting

#Explicit Typecasting - here, user does the conversion from one datatype to another

a = '1' #a is a string
b = 14  # b is a integer
print(int(a) + b)  # here, we did explicit typecasting to convert string datatype to integer


# Implicit typecasting - here, python does the typecasting automatically --here some data-type has higher order

a = 1   #integer
b = 2.5 # floating number
print(a + b)  #output is 3.5 , which is floating number as implicit typeconversion is done to var a
print(type(a+b)) # output-float