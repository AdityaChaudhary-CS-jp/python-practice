# Problem10
a = int(input('Cost of 1 Shirt = '))
b = int(input('Cost of 1 Jeans = '))
c = int(input('Quantity of Shirts = '))
d = int(input('Quantity of Jeans = '))
e = int(input('Discount in % = '))
print('--------------------------------------')
print('\t\tBILL')
print('--------------------------------------')
k = a*c
l = b*d
m = k+l
n = (m*e)/100
o = m-n
print('Amount of Shirts = ',k)
print('Amount of Jeans = ',l)
print('Total Amount = ',m)
print('Discount = ',n)
print('Amount to be Paid = ',o)
print('--------------------------------------')
print('\tThanks! Visit Again')
print('--------------------------------------')
