# Problem269
def febo(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return febo(a-1)+febo(a-2)
n = int(input('Enter the number of term = '))
for i in range(n):
    print(febo(i))
