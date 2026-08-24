# Problm260
def numb(k):
    if k==1:
        print(k)
    else:
        numb(k-1)
        print(k)
n = int(input('Enter Number = '))
p=numb(n)
