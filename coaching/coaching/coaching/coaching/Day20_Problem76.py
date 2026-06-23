# Problem76
a = int(input('Enter a number = '))
n = 0
for i in range(1,a+1):
      if a%i==0:
            n=n+1
if n == 2:
      print('Prime no.')
else:
      print('Not prime No.')

# OR

a = int(input('Enter a number = '))
f = 5 
for i in range(2,a):
      if a%i==0:
            f=10
            break
if f ==5:
      print('Prime No.')
else:
      print('Not Prime No.')

# OR
a = int(input('Enter a number = '))
n = 0
for i in range(2,a):
      if a%i==0:
           print('Not Prime No')
           break
else:
      print('Prime Number')
