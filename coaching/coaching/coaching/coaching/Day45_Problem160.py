# Problem160
a=input('Enter the sentence = ')
a=a+' '
i=0
while i<len(a)-1:
    if a[i] == a[i+1]:
        print(a[i],end='')
        i=i+1
    else:
        print(a[i],end='')
    i=i+1
