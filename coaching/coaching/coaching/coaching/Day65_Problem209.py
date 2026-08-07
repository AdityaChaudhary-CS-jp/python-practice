# Problem209
a = input('Enter the string = ')
h={}
for i in a:
    if i in h.keys():
        m=h[i]
        m=m+1
        h[i]=m
    else:
        h[i]=1
for i in h:
    c = list(h.keys())
    c.sort()

for i in c:
    print(i, h[i])
