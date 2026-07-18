# Problem161
a=input('Enter the word = ')
m=ord(a[0])
k=''
if m>=ord('a') and m<=ord('z'):
        k=chr(m-32)
else:
        k=a[0]
for i in range(1,len(a)):
        k=k+a[i]
print(k)
