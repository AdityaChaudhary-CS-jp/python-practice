# Problem155
a=input('Enter the Sentence = ')
a=a + ' '
k = ''
for i in a:
    if i==' ':
        print(k[0],'.',end='')
        k=''
    else:
        k=k+i
