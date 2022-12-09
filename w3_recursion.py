def try_recursion(k):
    if k>0:
        result = k + try_recursion(k-1)
        print (result)

    else:
        result = 0
    return result


print('\n\n Recursion Example Results: ')
try_recursion(6)