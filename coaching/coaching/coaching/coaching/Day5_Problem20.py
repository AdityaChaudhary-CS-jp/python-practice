# Problem20
a = int(input('Enter the days = '))
b = a//365
c = a%365
d = c//30
e = c%30
f = e//7
g = e%7
print(a,'days is equal to',b,'year(s),',d,'month(s),',f,'week(s) and',g,'day(s).')
