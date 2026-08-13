# Problem229
def lit(k):
    k[0],k[1]=k[1],k[0]
l=[]
for i in range(2):
    a = int(input('Enter the number = '))
    l.append(a)
print(l)
lit(l)
print(l)
