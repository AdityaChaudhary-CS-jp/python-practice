# Problem51
a = int(input("Enter 1st side : "))
b = int(input("Enter 2nd side : "))
c = int(input("Enter 3rd side : "))
if (a==b and b!=c) or (a==c and b!=c) or (b==c and a!=c):
    print("Isosceles triangle possible")
else:
    print("Isosceles triangle not possible")
