# Problem274
import csv
a=0
while a!=6:
    print('1.Add record')
    print('2.View record')
    print('3.Delete record')
    print('4.Update record')
    print('5.Search record Classwise')
    print('6.Exit')
    a=int(input('Enter your choice:'))
    if a==1:
        d=[]
        rn= input('Enter Roll No:')
        name= input('Enter Name:')
        ck= input('Enter Class:')
        email= input('Enter Email:')
        l=[rn,name,ck,email]
        d.append(l)
        b= open('record.csv','a',newline='')
        c= csv.writer(b)
        c.writerows(d)
        b.close()
    elif a==2:
        b= open('record.csv','r')
        c= csv.reader(b)
        for i in c:
            print(i)
        b.close()
    elif a==3:
        del_ = input('Enter Roll No of row which you wanys to delete:')
        b= open('record.csv','r')
        c= csv.reader(b)
        b1 = open('record1.csv','a',newline='')
        c1= csv.writer(b1)
        for m in c:
            if m[0]==del_:
                pass
            else:
                c1.writerow(m)
        b.close()
        b1.close()
        import os
        os.remove('record.csv')
        os.rename('record1.csv','record.csv')
        print('Record Deleted')
    elif a==4:
        name = input('Enter Name of student which you want to update:')
        b = open('record.csv','r')
        c = csv.reader(b)
        p = []

        for i in c:
            if i[1] == name:
                d = input('Enter new class:')
                e = input('Enter new email:')
                f = input('Enter new roll no:')

                i[0] = f
                i[2] = d
                i[3] = e

            p.append(i)

        b.close()

        b = open('record.csv','w',newline='')
        c = csv.writer(b)
        c.writerows(p)
        b.close()
    elif a==5:
        ck= input('Enter Class:')
        b= open('record.csv','r')
        c= csv.reader(b)
        d=5
        for i in c:
            if i[2]==ck:
                print(i)
                d=10
        if d==5:
            print('No record found')
    elif a==6:
        print('Thank you for using this program')
        break
    else:
        print('Invalid choice')
