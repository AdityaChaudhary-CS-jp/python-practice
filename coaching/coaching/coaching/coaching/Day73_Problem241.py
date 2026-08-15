# Problem241
a = open('Problem240.py')
b=''
m=''
c=9999999999999
p=' '
while p:
    p=a.readline()
    if p == '':
            break
    p = p + ' '
    for i in p:
        if i==' ':
            if len(m)>0 and len(m)<c:
                b=m
                c=len(m)
            m=''
        else:
            m=m+i
print('Smallest word = ',b)
