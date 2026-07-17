# Problem157
a=input('Enter the sentence = ')
a=a+' '
b=''
m=''
c=99999999
for i in a:
    if i==' ':
        if len(m)<c:
            b=m
            c=len(m)
            m=''
    else:
        m=m+i
print('shortest word = ',b)
print('Its length is = ',c)
