# Problem215
def gret (k,l,m):
    if k>l and k>m:
        print('Greatest number = ',k)
    elif l>k and l>m:
        print('Greatest number = ',l)
    else:
        print('Greatest number = ',m)
a = int(input('Enter 1st number = '))
b = int(input('Enter 2nd number = '))
c = int(input('Enter 3rd number = '))
gret(a,b,c)
