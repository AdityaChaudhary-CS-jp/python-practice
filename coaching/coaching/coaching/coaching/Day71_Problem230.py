# Problem230
def tdel (a,b):
    r = list(a)
    r.remove(b)
    r=tuple(r)
    return r
m = eval(input('Enter Tuple = '))
k = int(input('Number = '))
h = tdel(m,k)
print(h)
