# Problem256
# b= [name, rollno, sub1, sub2, sub3]
# Add nme of person to list b if average of sub1, sub2, sub3 is greater than or equal to 85
b=[]
def push_person(p):
    a = (p[2] + p[3] + p[4]) / 3
    if a>=85:
        b.append(p[0])
m=['abcd',98736,80,90,98]
push_person(m)
print(b)
