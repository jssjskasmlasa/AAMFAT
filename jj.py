lst = []

for i in range(1,101):
    lst.append(i)







cycle = 0
for n in lst:
    
    
    
    while n != 1 :
        
        
        
        
        if (n % 2 == 0):

            n = (n//2)

            print(n)

        else:
            n = 3*n + 1
            print(n)
        if n ==1:
            print('\n')