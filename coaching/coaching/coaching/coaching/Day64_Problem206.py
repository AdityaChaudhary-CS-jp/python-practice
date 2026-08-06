# Problem206
a=int(input('How Many persons = '))
h={}
for i in range(a):
    b=input('Enter the name = ')
    c = int(input('Enter mobile no. of person = '))
    h[b]=c
for i in h:
    print('Mobile no. of', i,'is',h[i])
