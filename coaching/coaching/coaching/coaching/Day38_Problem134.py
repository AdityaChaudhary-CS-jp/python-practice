# Problem134
a=int(input('Enter the number = '))
for i in range(1,a):
    k=a%i
    if k==0 and a//i==i+1 and a//(i+1)==i :
        print('Pronic number')
        break
else:
        print('Not pronic number')
