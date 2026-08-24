# Problem258
def me(n):
    if n==1:
        print(n)
    else:
        print(n)
        me(n-1)
a = int(input('Enter Number = '))
me(a)
