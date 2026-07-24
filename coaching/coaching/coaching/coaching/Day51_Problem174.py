# Problem174
a = input('Enter the sentence = ')
m = ''
a = a + ' '
for i in a:
    if i == ' ':
        if m:
            if len(m) == 1:
                b = m.upper()
            else:
                b = m[0].upper() + m[1:-1].lower() + m[-1].upper()
            print(b, sep='', end=' ')
        m = ''
    else:
        m = m + i
