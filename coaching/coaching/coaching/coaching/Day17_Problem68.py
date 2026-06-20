# Problem68
n = int(input('Enter a number = '))
for i in range(1,n+1):
    if i==n:
        print('(',i,'^',i+1,')','=',sep='' )
    else:
        print('(',i,'^',i+1,')',sep='',end=' + ')
