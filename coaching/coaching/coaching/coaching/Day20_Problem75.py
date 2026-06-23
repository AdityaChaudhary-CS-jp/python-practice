# Problem75
a = int(input('Enter a number = '))
n = 0
for i in range(1,a+1):
      if a%i==0:
            n=n+1
print('No. of factors of',a,'are',n)
