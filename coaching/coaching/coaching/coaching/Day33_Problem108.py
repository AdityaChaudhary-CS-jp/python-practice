# Problem108
a= int(input('Enter the start number  = '))
b= int(input('Enter the end number  = '))
for i in range(a,b+1):
    for j in range(i+1,b+1):
        for k in range(j+1,b+1):
            if k*k==(j*j+i*i):
                print(i,j,k)
