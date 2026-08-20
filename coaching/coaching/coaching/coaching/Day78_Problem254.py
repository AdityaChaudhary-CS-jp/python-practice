# Problem254
try:
    a = int(input('How many Elements ='))
    l=[]
    for i in range(a):
        print('Enter',i+1,'Number',end=' ')
        b = int(input(' = '))
        l.append(b)
    c = int(input('Enter numerator index = '))
    d = int(input('Enter denominator index = '))
    e = l[c]/l[d]
    print(e)
except ValueError:
    print('Enter Number Only')
except IndexError:
    print('Out of range index')
except ZeroDivisionError:
    print('Denominator is zero')
print('All error Covered')
