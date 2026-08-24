# Problem259
def su(k):
    if k==0:
        return 0
    else:
        return k + su(k-1)
a = int(input('Enter Number = '))
print('Sum of First',a,'Natural Numbers =',su(a))
