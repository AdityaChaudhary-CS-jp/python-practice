# Problem152
a = input("Enter the name = ")
k = 0
for i in a:
    if i == " ":
        print('\t',k)
        print()
        k = 0
    else:
        print(i, end="")
        k = k + 1

print('\t',k)
