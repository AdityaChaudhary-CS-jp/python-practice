# Problem153
# Method 2 of Problem152
a=input('Enter the Sentence = ')
a=a + ' '
k = ''
for i in a:
    if i==' ':
        print(k,len(k))
        k=''
    else:
        k=k+i
