# Problem270
def show(a, i):
    if i == len(a):
        return
    else:
        print(a[:i+1])
        show(a, i+1)

a = input('Input a string = ')
show(a, 0)
