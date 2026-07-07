# Problem115
p=int(input('Enter the no = '))
k=1
while p!=0:
    r=p%10
    p=p//10
    k*=r
print(k)
