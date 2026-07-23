# Problem171
a = input('Enter the sentence = ')
m=''
a=a+' '
for i in a:
    if i==' ':
        if m.isdigit():
            k=int(m)
            print(k*2)
        else:
            print(m*3)
        m=''
    else:
        m=m+i
