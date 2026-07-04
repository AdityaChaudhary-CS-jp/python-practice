#Problem98
a=int(input('How many rows = '))
b =int(input('How many columns = '))
p=ord('a')
for i in range(1,a+1):
    print(chr(p),end=' ')
    for j in range(1,b-1):
        print('#',end=' ')
    print(i,end=' ')
    print()
    p=p+1
