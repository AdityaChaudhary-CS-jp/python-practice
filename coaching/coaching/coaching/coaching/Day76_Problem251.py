# Problem251
import csv
a = open('new.csv','w')
b = csv.writer(a)
l =[24,28,87,98,78]
b.writerow(l)
k=[[12,8787,28],[45,89,39],[55,8,38,2]]
b.writerows(k)
a.close()
# a = open('new.csv','a',newline='')   ise this to remve the extra line in the csv file
import csv
a =open('new.csv','r')
b = csv.reader(a)
for i in b:
    print(i)
a.close()
