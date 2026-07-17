# Problem159
a=input('Enter the sentence = ')
m=''
for i in range(len(a)-1,-1,-1):
    m=m+a[i]
if a==m:
    print('Palindrome')
else:
    print('Not Palindrome')
