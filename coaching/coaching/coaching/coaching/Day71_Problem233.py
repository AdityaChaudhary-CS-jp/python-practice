# Problem233
a =open('Problem232.py','r')
m=a.read()+' '
p=0
for i in m:
    if i == ' ':
        p=p+1
print(p+1)
