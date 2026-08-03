# Problem204
t = (5, 10, 15)
k=list(t) # Convert tuple to list, perform list operations, then convert it back to tuple.
k.append(20)
t=tuple(k)
print(t)
