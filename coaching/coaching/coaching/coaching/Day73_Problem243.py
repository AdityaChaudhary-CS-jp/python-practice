# Problem243
a = open('Problem242.py')
p= ' '
while p :
    p=a.readline()
    if p == '':
        break
    p=p.strip()
    if p[0] in 'aeiou' and p[-1] not in 'aeiou':
        print(p)
