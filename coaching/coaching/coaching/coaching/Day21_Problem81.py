# Problem81
a = int(input('Enter How many time to display = ' ))
p= 999999999
for i in range(a):
    b = int(input('Enter the number = '))
    if b<p:
     p=b
print('Smallest number is ',p)
