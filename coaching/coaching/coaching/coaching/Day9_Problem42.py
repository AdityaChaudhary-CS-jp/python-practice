# Problem42
a = int(input("Enter a length: "))
b = int(input("Enter a breath: "))

print("1 / a / A : Area")
print("2 / p / P : Perimeter")
print("3 / b / B : Both")

K = input("Enter Your choice: ")
if K == '1' or K == 'a' or K == 'A':
    print("Area:", a * b)
if K == '2' or K == 'p' or K == 'P':
    print("Perimeter:", 2 * (a + b))
if K == '3' or K == 'b' or K == 'B':
    print("Area:", a * b)
    print("Perimeter:", 2 * (a + b))
