# Problem145
a=input('Enter the name = ')
p=0
for i in a:
    if i in 'aeiou' or i in 'AEIOU':
        p=p+1
print('Total Vowels in sentences = ',p)
