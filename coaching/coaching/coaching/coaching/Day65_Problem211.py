# Problem211
a = int(input('How many players = '))
h={}
for i in range(a):
    print('--------------------')
    print('PLAYER',i+1)
    print('--------------------')
    nam = input('Enter Player name = ')
    l=[]
    for j in range(3):
        print('Enter',j+1,'inning score',end=' ')
        inn=int(input(' = '))
        l.append(inn)
        h[nam]=l
print('NAME',':','TOTAL, HIGHEST, LOWEST ')
for i in h:
    p=h[i]
    e=max(p)
    f=min(p)
    print(i,':',sum(p),',',max(p),',',min(p))
