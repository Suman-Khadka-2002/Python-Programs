# Implementing match-case 

x = int(input("Enter the value of x: "))
# x is the variable to match

match x:
# if x is 0
    case 0:
        print("x is zero")   
 # if x is 4
    case 4:
        print("case is 4") 
        
# case with if-condition

    # case _ if x!=40:
    #     print(x, " is not 40") 
    # case _ if x!=80:
    #     print(x, " is not 80")
    case _ if x<10:
        print(x, " is <10")
    case _ if x%2 ==0:
        print("x % 2 == 0 is true")

        # default case will only be matched if above case will not match
    case _:
        print(x)
