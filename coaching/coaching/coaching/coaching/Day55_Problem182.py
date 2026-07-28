# Problem182
a = int(input('How many numbers = '))
l = []
for i in range(a):
    print('Enter ', i + 1,'number' , end='')
    c = int(input(' : ')) 
    l.append(c)
print(l)
odd=[]
even=[]
for i in l:
    if i%2==0:
        d=i
        even.append(d)
    else:
        e=i
        odd.append(e)
print('Even numbers:', even)
print('Odd numbers:', odd)
