# Problem166
a = input('Enter the sentence = ')
a=a+' '
m=''
c=0
for i in a:
    if i==' ':
        if len(m)>c:
            c=len(m)
        m=''
    else:
        m=m+i
m=''
for i in a:
    if i==' ':
        if len(m)==c:
            print(m)
        m=''
    else:
        m=m+i
