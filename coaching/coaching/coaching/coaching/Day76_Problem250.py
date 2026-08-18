# Problem250
a = open('Problem248.py', 'rb')
a.seek(5)
b = a.read()
print(b)
a.seek(-50, 1)
b = a.read(5)
print(b)
print(a.tell())
