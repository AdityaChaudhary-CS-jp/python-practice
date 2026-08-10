# Problem219
def fac(k):
    f=1
    for i in range(1,k+1):
        f=f*i
    return f
a = int(input('Enter How many numbers = '))
k=0
for i in range(1,a+1):
    k=k+i/fac(i)
print(k)
