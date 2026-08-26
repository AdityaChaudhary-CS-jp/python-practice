# Problem266
def gap(a, b, c):
    if ord(a) <= ord(b):
        print(a)
        k = ord(a)
        k = k + c
        a = chr(k)
        gap(a, b, c)

x = int(input('Enter the gap = '))
y = input('Enter the ENDING character = ')

gap('A', y, x)
