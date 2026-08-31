# Problem272
def addf(filename,stack):
    # add unique name in stack and return
    import csv
    a=open(filename,'r',newline='')
    b=csv.reader(a)
    p=[]
    for i in b:
        p.append(i[0])
    if stack[0] not in p:
        a=open(filename,'a',newline='')
        c=csv.writer(a)
        c.writerow(stack)
        a.close()
