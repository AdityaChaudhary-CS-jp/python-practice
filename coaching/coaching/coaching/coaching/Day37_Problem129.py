# Problem129
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = 2
while c <a:
    if a % c == 0 and b % c == 0: 
           print("Not Co-Prime Numbers")
           break
    else:
          print("Co-Prime Numbers")
          break
