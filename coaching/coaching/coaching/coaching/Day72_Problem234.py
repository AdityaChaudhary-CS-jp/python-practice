# Problem234
a = open('Problem233.py','r')
m = a.read()
p=0
for i in m:
    if i in 'aeiou':
        p=p+1
print('Count of vowels = ',p)
