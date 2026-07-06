# Problem107
a= int(input('How many rows = '))
for i in range(a):
    p = ord('A')
    for j in range(i):
        print(' ',end=' ')
    for k in range(a-i):
        l = chr(p)
        print(l,end=' ')
        p+=1
    p-=1
    for m in range(a-i-1):
        p-=1
        print(chr(p),end=' ')
        
    print()
