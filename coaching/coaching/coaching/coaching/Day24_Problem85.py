# Problem85
a=int(input('Enter the start no.'))
b=int(input('Enter the end no.'))
for i in range (a,b+1):
    p=0
    for j in range(1,i+1):
        if i%j==0:
            p=p+1
    if p==2:
      print(i)
    
