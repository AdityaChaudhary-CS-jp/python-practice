# Problem242
a = open('Problem241.py')
p=' '
while p:
    p=a.readline()
    d=p.strip()
    for i in d :
         if d[0]=='p':
              print(p)
              break
