# Problem66
a =int(input('Enter a number = '))
b =int(input('Enter a number = '))
if a<b:
    for i in range(a,b+1,2):
      print(i,end = ' ')
else:
    for i in range(a,b-1,-3):
        print(i,end=' ')
