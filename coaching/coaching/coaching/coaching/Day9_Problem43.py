# Problem43
a = int(input("Enter 1st Subject Marks: "))
b = int(input("Enter 2nd Subject Marks: "))
c = int(input("Enter 3rd Subject Marks: "))
d = int(input("Enter 4th Subject Marks: "))
e = int(input("Enter 5th Subject Marks: "))

total_marks = a + b + c + d + e
f = total_marks / 500
g = f * 100

print("Total marks =", total_marks)
print("Total percentage =", g)

if g >= 75:
    print("Rank = Distinct")

if g >= 65 and g < 75:
    print("Rank = First")

if g >= 45 and g < 65:
    print("Rank = Second")

if g >= 35 and g < 45:
    print("Rank = Third")

if g < 35:
    print("Rank = FAIL")
