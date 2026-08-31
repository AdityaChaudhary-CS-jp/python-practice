# Problem271
'''
All Operation in a file
'''
def writerf(filename,k):
    # k nested list record add in filename
    import csv
    a=open(filename,'a',newline='')
    b=csv.writer(a)
    b.writerows(k)
    a.close()
