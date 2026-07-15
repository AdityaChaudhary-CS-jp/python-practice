# Problem148
#PRINT ONLY FIRST INDEX OF CHARACTER IN STRING
#PRINT ONLY SECOND INDEX OF CHARACTER IN STRING
#PRINT ONLY LAST INDEX OF CHARACTER IN STRING
a=input('Enter the name = ')
b=input('Enter the character = ')
for i in range(len(a)):
    if a[i] == b:
        print(i)
        break
