# Problem162
a=input('Enter the sentence = ')
m=ord(a[0])
k=''
if m>=ord('a') and m<=ord('z'):
    k=chr(m-32)
else:
    k=a[0]
for i in range(1,len(a)):
    if a[i-1]==' ':
        m=ord(a[i])
        if m>=ord('a') and m<=ord('z'):
            k=k+chr(m-32)
        else:
            k=k+a[i]
    else:
        k=k+a[i]
print(k)
