# Problem253
try:
   l =[25,87,89,2]
   i = int(input('Enter Index You want to display= '))
   m=l[i]
   print(m)
except IndexError:
   print('Out of range index')
try:
  a = input('Enter the number = ')
  b= input('Enter the number = ')
  c = int(a) + int(b)
  print(c)  
except ValueError:
   print('Enter Numbr Only')
try:
   print('Enter Number Only')
   k =open('login.py','r')
   print(k.read())
except FileNotFoundError:
   print('File Not Found check it\'s name properly')
