# Problem207
a = int(input('How many state\'s = ' ))
p ={}
for i in range(a):
    b=input('Enter the name of state = ')
    c=input('Enter the capital of state = ')
    p[b]=c
print(p)
d = input('Enter any state name = ')
if d in p.keys():
    print(d,'capital is',p[d])
else:
    b = input('Enter the name of Capital = ')
    p[d]=b
    print(d,'capital is',p[d])
