# Problem246
a = 0
while a!=6:
    print('\n---MENU---')
    print('1.Add Record')
    print('2.View all Record')
    print('3.Search by Aadhar')
    print('4.Search by Name')
    print('5.Search by Age in range')
    print('6.Exit')
    a = int(input('Choice = '))
    if a==1:
        aadhar=input('Enter Aadhar number = ')
        name = input('Enter Name = ')
        city = input('Enter City = ')
        age = input('Enter age = ')
        b = open('Aadhar.dct','a')
        d = aadhar + ' ' + name + ' ' + city + ' ' + age + '\n'
        b.write(d)
        b.close()
        print('Record added')
    elif a==2:
        print('\n---All Record---')
        b = open('Aadhar.dct')
        p = ' '
        while p:
            p= b.readline()
            print(p,end=' ')
        b.close()
    elif a==3:
        c = input('Enter Your aadhar number = ')
        b = open('Aadhar.dct')
        p = ' '
        e = 5
        while p:
            p = b.readline()
            if p == '':
                break
            k = p.strip().split()
            if k[0] == c:
                print(k)
                e = 10
                break
        if e == 5:
            print('No Record Found')
        b.close()
    elif a==4:
        f = input('Enter Your Name = ')
        b = open('Aadhar.dct')
        p = ' '
        e = 5
        while p:
            p = b.readline()
            if p == '':
                break
            k = p.strip().split()
            if k[1] == f:
                print(k)
                e = 10

        if e == 5:
            print('No Record Found')
        b.close()
    elif a==5:
        min_ = int(input('Enter minimum Age = '))
        max_ = int(input('Enter maximum Age = '))
        b= open('Aadhar.dct')
        p=' '
        while p:
            p=b.readline()
            if p == '':
                break
            k=p.strip().split()
            if int(k[3]) >= min_ and int(k[3]) <= max_:
                print(k)
        else:
            print('No Record')
    elif a==6:
        print('Exiting Aadhar Records')
    else:
        print('Invalid Choice')
