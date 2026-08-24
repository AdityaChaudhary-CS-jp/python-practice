# Problem261
def numb(k):
    if k==1:
        print(k)
    else:
        print(k)
        numb(k-1)
n = int(input('Enter Number = '))
p=numb(n)
