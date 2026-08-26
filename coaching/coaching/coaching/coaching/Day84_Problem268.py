# Problem268
def vert(a,k):
    if k==len(a)-1:
        print(a[k])
    else:
        print(a[k])
        k=k+1
        vert(a,k)
m = input('Enter the string = ')
s = vert(m,0)
