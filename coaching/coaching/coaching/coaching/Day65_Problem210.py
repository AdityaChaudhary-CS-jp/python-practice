# Problem210
a = int(input('How many players = '))
b = int(input('How many innings = '))
h={}
for i in range(a):
    print('--------------------')
    print('PLAYER',i+1)
    print('--------------------')
    nam = input('Enter Player name = ')
    l=[]
    for j in range(b):
        print('Enter',j+1,'inning score',end=' ')
        inn=int(input(' = '))
        l.append(inn)
        h[nam]=l
for i in h:
    p=h[i]
    print('NAME',':','TOTAL')
    print(i,':',sum(p))
