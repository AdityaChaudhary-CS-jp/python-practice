# Problem168
a = input('Enter the name = ')
b = int(input('How many last alphabts = '))
k = a[-b:]
p=k[::-1]
print('Last alphabes Left ---> Right = ',k)
print('Last alphabes Right ---> Left = ',p)
