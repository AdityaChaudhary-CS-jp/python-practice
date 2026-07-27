# Problem180
a = int(input('How many Numbers/string = '))
b = []
for i in range(a):
    c  = (input('Enter the list = '))
    b.append(c)
print(b)
for i in b :
    if i.isdigit():
        k=int(i)
        print(k*2)
    else:
        print(i*3)
