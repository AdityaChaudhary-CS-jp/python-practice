# Problem236
k = open('Problem235.py','r')
m = k.read() + ' '
i=0
p=0
while i<len(m)-1:
    if m[i]==m[i+1]:
        p=p+1
    i=i+1
print(p)
