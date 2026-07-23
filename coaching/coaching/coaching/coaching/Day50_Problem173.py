# Problem173
a = input('Enter the sentence = ')
m = ''
a = a + ' '
for i in a:
    if i == ' ':
        if m:
            print(m[0].upper(), m[1:].lower(), sep='',end=' ')
        m = ''
    else:
        m = m + i
