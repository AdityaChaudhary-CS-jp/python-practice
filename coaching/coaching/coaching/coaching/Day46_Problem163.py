# Problem163
a = input('Enter the sentence = ')
a = a + ' '
k = ''
i = 0
while i < len(a):
    if a[i] == ' ':
        if i != len(a)-1:
            m = ord(k[0])
            if m >= ord('a') and m <= ord('z'):
                print(chr(m-32), end='')
            else:
                print(k[0], end='')
            k = ''
        else:
            m = ord(k[0])
            if m >= ord('a') and m <= ord('z'):
                print(' ', chr(m-32), end='', sep='')
            else:
                print(' ', k[0], end='', sep='')

            j = 1
            while j < len(k):
                print(k[j], end='')
                j = j + 1
    else:
        k = k + a[i]
    i = i + 1
