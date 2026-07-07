# Problem114
p=int(input('Enter the no = '))
k=0
while p!=0:
    r=p%10
    p=p//10
    k+=r
print(k)
