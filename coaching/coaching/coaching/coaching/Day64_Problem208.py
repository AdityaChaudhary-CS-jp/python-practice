# Problem208
a = input('Enter the string = ')
h = {}
for i in a:
    if i in h.keys():
        m=h[i]
        m=m+1
        h[i]=m
    else:
        h[i]=1
for i in h:
    print(i,h[i])
