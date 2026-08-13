# Problem232
def lcomp():
    k=set(a)
    l=set(b)
    if k==l:
        return 1
    else:
        return -1
a = eval(input('Enter 1st list = '))
b = eval(input('Enter 2nd list = '))
k= lcomp()
print(k)
