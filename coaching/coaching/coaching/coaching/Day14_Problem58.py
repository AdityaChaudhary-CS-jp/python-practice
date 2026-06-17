# Problem58
a = int(input("Enter year: "))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("Leap year (century leap year)")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
