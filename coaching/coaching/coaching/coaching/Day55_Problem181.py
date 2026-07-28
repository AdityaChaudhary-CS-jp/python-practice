# Problem181
a = int(input('How many numbers = '))
l = []
for i in range(a):
    print('Enter ', i + 1,'number' , end='')
    c = int(input(' : ')) 
    l.append(c)
b=l
print('List Left to Right:', b)
c=b[::-1]
print('List Right to Left:', c)
