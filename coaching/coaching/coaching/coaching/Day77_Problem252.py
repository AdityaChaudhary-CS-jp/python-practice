# Problem252
a=0
import csv
b=open('Record.csv','a',newline='')
c = csv.writer(b)
l='id'  ,  'name'  ,  'company'  ,  'price'
k = 783,'AC','LG',20000
m = 258,'TV','Samsung',25000
c.writerow(l)
c.writerow(k)
c.writerow(m)
b.close()
while a!=5:
    print('1. Enter 5 Record ;2 in code other 3 in run time')
    print('2.Display all Record')
    print('3.Display only name ,price')
    print('4.Search by Company name')
    print('5.Exit')
    a=int(input('Enter your choice = '))
    if a==1:
        d=[]
        for i in range(3):
            id_ = input('Enter id = ')
            name = input('Enter name = ')
            company = input('Enter company = ')
            price =input('Enter price = ')
            d.append([id_,name,company,price])
        print('Registered Successfully')
        b=open('Record.csv','a',newline='')
        c = csv.writer(b)
        c.writerows(d)
        b.close()
    elif a==2:
        b=open('Record.csv','r')
        c = csv.reader(b)
        for i in c:
            print(i)
        b.close()
    elif a==3:
        b=open('Record.csv','r')
        c = csv.reader(b)
        next(c)
        for i in c:
            print(i[1],i[3])
        b.close()
    elif a==4:
        d = input('Enter Company Name = ')
        b = open('Record.csv','r')
        c=csv.reader(b)
        next(c)
        e =5
        for i in c:
            if d==i[2]:
                print(i)
                e=10
        if e==5:
            print('Company Not Found')
    elif a==5:
        print('Exiting')
    else:
        print('Wrong Choice')
