# Problem154
a=input('Enter the Sentence = ')
a=' ' + a
k = ''
for i in range(len(a)-1,-1,-1):
    if a[i]==' ':
        for j in range(len(k)-1,-1,-1):
          print(k[j],end='')
        print(len(k))
        k=''
    else:
        k=k+a[i]
