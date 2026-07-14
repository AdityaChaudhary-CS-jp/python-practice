# Problem146
a=input('Enter the name = ')
p=0
for i in a:
    if i in '0123456789':
        p=p+1
print('Total digits in sentences = ',p)
