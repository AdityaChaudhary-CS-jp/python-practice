# Problem267
def reverse(a,k):
    if k==-len(a):
        print(a[k])
    else:
        print(a[k])
        k=k-1
        reverse(a,k)
n = input('Enter the string = ')
r = reverse(n,-1)
