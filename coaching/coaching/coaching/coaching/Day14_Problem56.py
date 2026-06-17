# Problem56

a = input('Choice (1 or w = Week, 2 or m = Month): ')

if a == '1' or a == 'w':
    print('Week')
    b = int(input('enter week day : '))

    if b == 1:
        print('Sunday')
    elif b == 2:
        print('Monday')
    elif b == 3:
        print('Tuesday')
    elif b == 4:
        print('Wednesday')
    elif b == 5:
        print('Thursday')
    elif b == 6:
        print('Friday')
    elif b == 7:
        print('Saturday')
    else:
        print('Invalid week day')

elif a == '2' or a == 'm':
    print('Month')
    c = int(input('enter month (1-12): '))

    if c == 1:
        print('January')
    elif c == 2:
        print('February')
    elif c == 3:
        print('March')
    elif c == 4:
        print('April')
    elif c == 5:
        print('May')
    elif c == 6:
        print('June')
    elif c == 7:
        print('July')
    elif c == 8:
        print('August')
    elif c == 9:
        print('September')
    elif c == 10:
        print('October')
    elif c == 11:
        print('November')
    elif c == 12:
        print('December')
    else:
        print('Invalid month')

else:
    print('Invalid choice')

