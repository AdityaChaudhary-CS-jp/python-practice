# Problem165
a = input('Enter the sentence = ')
k=''
for i in a:
    if i==' ':
        m=ord(k[0])
        if m>=ord('a') and m<=ord('z'):
              k=chr(m-32)
        print(k,end='')
        k=''
    else:
        k=k+i
print(' ',k)x
