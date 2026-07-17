# Problem158
a=input('Enter the sentence = ')
a=a+' '
m=''
for i in a:
    if i==' ':
        if m[0]==m[-1]:
         print(m)
        m=''
    else:
        m=m+i
