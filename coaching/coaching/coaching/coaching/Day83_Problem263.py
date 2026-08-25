# Problem263
def fac(k):
    if k==1:
        return 1
    else:
        return k*fac(k-1)
n = int(input("Enter a number =  "))
r = fac(n)
print(r)
