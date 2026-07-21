# Problem164
a = input('Enter the name = ')
k=''
for i in a:
    if i==' ':
        print(k[0],end='')
        k=''
    else:
        k=k+i
else:
    print(' ',k)
