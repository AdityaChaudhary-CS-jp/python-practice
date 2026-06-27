# Problem86
a=int(input('Enter the start no.'))
b=int(input('Enter the end no.'))
for i in range (a,b+1):
    c=int(i/2)+1
    for j in range(1,c):
        if j*j==i:
            print(i)
