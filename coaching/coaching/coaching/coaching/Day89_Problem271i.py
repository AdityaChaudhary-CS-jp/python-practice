import Problem271
d=[]
name = input('Enter the name = ')
id_ = int(input('Enter the id = '))
mobile = int(input('Enter the mobile number = '))
email = input('Enter the email = ')
pin = int(input('Enter the pincode = '))
l=[name,id_,mobile,email,pin]
d.append(l)
Problem271.writerf('**.csv',d)
