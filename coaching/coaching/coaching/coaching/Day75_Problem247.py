# Problem247
a = 0
import pickle 
while a!=5:
    print('\n---MENU---')
    print('1.Register a Book')
    print('2.View all Record')
    print('3.Search by Author')
    print('4.Search by Id')
    print('5.Exit')
    a = int(input('Choice = '))
    if a==1:
        bookid=input('Enter Book Id = ')
        name = input('Enter Your Name = ')
        author = input('Enter Author Name  = ')
        price = input('Enter Book Price = ')
        quantity = input('How many Books = ')
        l=[]
        l.append(bookid)
        l.append(name)  
        l.append(author)
        l.append(price)
        l.append(quantity)
        b = open('Book.dat','ab')
        pickle.dump(l,b)
        b.close()
        print('Book Registered')
    elif a == 2:
        b = open('Book.dat', 'rb')
        h = pickle.load(b)
        print(h[0], h[1], int(h[3]) * int(h[4]))
        b.close()
    elif a == 3:
        d = input('Enter Author Name = ')
        b = open('Book.dat', 'rb')
        k = pickle.load(b)

        if k[2] == d:
            print(k)
        else:
            print('No Record Found')

        b.close()
    elif a == 4:
        d = input('Enter Book Id = ')
        b = open('Book.dat', 'rb')
        k = pickle.load(b)
        if k[0] == d:
            print(k)
        else:
            print('No Record Found')

        b.close()
    elif a==5 :
        print('Exiting')
    else:
        print('Invalid Choice Try Again')
