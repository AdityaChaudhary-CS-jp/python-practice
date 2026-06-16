# Problem54
a = input('Enter Your Gender : (Male/Female) = ')
b = float(input('Enter Your Weight = '))
c = float(input('Enter Your Height = '))
if a=='Male' and (b>45 and b <65) and (c>150 and c<180) :
    print('SELECTED')
elif a == 'Female' and (b>40 and b<60) and (c>130 and c<160):
    print('SELECTED')
else :
    print(' NOT SELECTED')
