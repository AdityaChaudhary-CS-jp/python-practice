#Problem45
a = int(input('Enter the Electricity Unit : '))
if a<=150:
    print('Total amount = ',a*5)
if a>150 and a<400 :
    b = 150*5 + (a-150)*2
    print('Total amount = ',b)
if a>=400 and a<700 :
    c = 150*5 + 250*2 + (a-400)*1
    print('Total amount = ',c)
if a>=700 :
    d = 150*5 + 250*2 + 300*1 + (a-700)*0.5
    print('Total amount = ',d)
