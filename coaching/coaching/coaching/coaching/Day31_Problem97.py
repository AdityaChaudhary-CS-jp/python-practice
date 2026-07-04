#Problem97
a=int(input('How many rows = '))
b =int(input('How many columns = '))
for i in range(a):
	for j in range(b):
		if (i+j)%2==0:
			print('1', end='')
		else:
			print('0', end='')
	print()
