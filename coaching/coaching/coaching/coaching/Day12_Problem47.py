# Problem47
a = int(input('Enter 1st Side: '))
b = int(input('Enter 2nd Side: '))
c = int(input('Enter 3rd Side: '))
if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
	print('Pythogorus Triplet possible')
else:
	print('Not Possible')  
