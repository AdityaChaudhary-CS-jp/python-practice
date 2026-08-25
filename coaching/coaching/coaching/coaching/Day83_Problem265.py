# Problem265
def alpha(a):
    if a=='Z':
        print('Z')
    else:
        print(a)
        k=ord(a)
        k=k+1
        a=chr(k)
        alpha(a)
alpha('A')
