# Problem262
def even(a,b):
    if a>b:
        pass
    else:
        print(a)
        even(a+2,b)
n = int(input('Enter ending Number = '))
even(2,n)
