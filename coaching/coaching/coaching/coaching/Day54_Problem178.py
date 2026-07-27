# Problem178
a = int(input('How many Numbers = '))
b = []
for i in range(a):
    print('Enter',i+1,'Number ',end=' ')
    c  = int(input('='))
    b.append(c)
print(b)
d = int(input('Enter any number = '))
e=0
if d in b :
    for i in b:
        if i==d:
            e=e+1
    print(d,'is',e,'times in',b)
else:
    print(d,'is zero times in',b)
