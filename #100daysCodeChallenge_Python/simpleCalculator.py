# simple calculator that does basic operations


a = int(input(""))
op = input("enter the operator: ")
b = int(input(""))

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
elif op == '%':
    print(a%b)