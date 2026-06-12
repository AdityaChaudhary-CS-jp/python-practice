# Problem44
a = int(input("Enter the amount: "))

if a <= 5000:
    print("Your Discount is 15 percent")

if a > 5000 and a < 20000:
    print("Your Discount is 25 percent")

if a >= 20000 and a < 50000:
    print("Your Discount is 40 percent")

if a >= 50000:
    print("Your Discount is 55 percent")

b = int(input("Enter the displayed Discount: "))
c = (a * b) / 100
print("Discount in Rupees is", c)

d = a - c
print("Amount to be paid =", d)

if a <= 5000:
    print("Your gift is diary")

if a > 5000 and a < 20000:
    print("Your gift is pen")

if a >= 20000 and a <= 50000:
    print("Your gift is bag")

if a >= 50000:
    print("Your gift is phone")
