# Problem255
s=[]
while True:
    print('1.Push')
    print('2.Pop')
    print('3.Traverse')
    a = int(input('Enter your choice = '))
    if a==1:
        b = int(input('Enter Number = '))
        s.append(b)
    elif a==2:
        if s==[]:
            print('Stack is Empty')
        else:
            print('Popped Element =',s.pop())
    elif a==3:
        if s==[]:
            print('Stack is Empty')
        else:
            print('Stack Elements =',s)
    else:
        print('Invalid Choice')
        break
