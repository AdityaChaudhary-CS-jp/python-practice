# Problem73
a = int(input('Enter the term = '))
if a%2==0:
    for i  in range(a,1,-2):
          print(i,end=' ')
else:
    for i in range(a-1,1,-2):
         print(i,end=' ')
