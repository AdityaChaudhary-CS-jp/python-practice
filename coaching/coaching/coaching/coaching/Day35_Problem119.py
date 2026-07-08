# Problem119

a = int(input('Enter the number = '))
p = a
d = a
print("Right to Left:")
while a != 0:
    r = a % 10
    a = a // 10
    print(r)
k = 0
while p != 0:
    r = p % 10
    p = p // 10
    k = k * 10 + r
print("Left to Right:")
while k != 0:
    r = k % 10
    k = k // 10
    print(r)
