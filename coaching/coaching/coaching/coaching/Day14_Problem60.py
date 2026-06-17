# Problem60
a = int(input("Enter a number: "))

if a >= 5  and a <= 3000:
    if a < 10:
        print("1 digit")
    elif a < 100:
        print("2 digits")
    elif a < 1000:
        print("3 digits")
    else:
        print("4 digits")
else:
    print("out of range")   
