# Problem167
a = input('Enter the word = ')
k=a[0:len(a)]
p=a[::-1]
if k==p:
    print('Palindrome')
else:
    print('Not Palindrome')
