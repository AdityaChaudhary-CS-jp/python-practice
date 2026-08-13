# Problem231
def strev():
    global a
    global b
    global k
    if k==b:
        return 1
    else:
        return -1
a = int(input('Enter the number = ')) 
b=a
k=0
while a!=0:
    r=a%10
    a=a//10
    k=k*10+r
result = strev()
print("Result:", result)
