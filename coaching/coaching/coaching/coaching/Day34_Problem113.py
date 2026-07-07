# Problem113
a= int(input('How many rows  = '))
p=ord('a')
i=0
while i<a:
    j=0
    while j<=i:
        print(chr(p),end=' ')
        j=j+1
    print()
    i=i+1
    p=p+1
