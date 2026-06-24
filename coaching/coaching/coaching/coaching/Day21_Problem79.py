# Problem79
a = int(input('How many time to display = '))
p=-1
for i in range(a):
    b = int(input('Enter a number = '))
    if b>p:
        p=b
print(p)
