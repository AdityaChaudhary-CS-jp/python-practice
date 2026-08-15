# Problem240
a = open('Problem239.py')
b = ''
m=''
c=0
p=' '
while p:
    p =a.readline()
    if p == '':
            break
    
    p = p + ' '
    
    for i in p:
        if i==' ':
            if len(m)>c:
                b=m
                c=len(m)
            m=''
        else:
            m=m+i
print('Longest word = ',b)
print('It\'s length = ',c)
