
 
def fibonnaci(n):
    if n == 1:
        return 1

    elif n == 2:
        return 2

    elif n > 2 :
        return fibonnaci(n-1) + fibonnaci((n-2))
    
for n in range(9):
    print(fibonnaci(n))


     