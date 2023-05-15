import csv
from datetime import datetime
from datetime import date

names={}
#create an empty dictionary theta will store name values pairs
#key-> enrollment number
#value-> name of the student


with open("namelist.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        names.update({line[1]:line[0]})

    #enrollmentnumber->name    

for keys in names.keys():
    print(keys+" "+names[keys])

print("\n")

# names2={}
# with open("namelist2.csv","r",newline="") as csv_file2:
#     csv_reader2=csv.reader(csv_file2)

#     next(csv_reader2)
#     for line in csv_reader2:
#         names2.update({line[1]:line[0]})

# for keys in names2.keys():
#     print(keys+" "+names2[keys])

# print("\n")

#we consider namelist as the file as qr code entry that contains the maximum number of entries
# we will update the final list according to that

#names and names2 two dictionaries -> compare 
#convention
#if a name is present in names2 but not in names it means proxy
#if a name is present in both mark present
#name not present in names2 and names mark absent


rows=[] #2-d matrix ith row will contain info of ith student , n rows where n=no of students

with open("finalnamelist.csv","r") as readfile:
    csv_reader=csv.reader(readfile)
    for line in csv_reader:
        rows.append(line)

curdate=str(date.today())
print(curdate)

if len(rows[0])>3:
    #erase the last row
    for i in range(len(rows)):
        rows[i].pop()

for i in range(len(rows)):
    if i==0:
        rows[0].append(curdate)
        continue

    id=rows[i][1]
    # print(id)
    ok1=False
    ok2=False
    if id in names.keys():
        ok1=True    
    # if id in names2.keys():   
    #     ok2=True

    # print(ok1)
    # print(ok2)    
    # if ok2==True and ok1==True:
    #     rows[i].append("Present")
    # elif ok2==False and ok1==True:    
    #     rows[i].append("Proxy")
    # else:
    #     rows[i].append("Absent")

    if ok1==True:
        rows[i].append("Present")
    else:
        rows[i].append("Absent")    

#store total attendance
for i in range(len(rows)):
    if i==0:
        rows[i].append("Total Attendance")
        continue

    count=0
    for j in range(len(rows[i])):
        if rows[i][j]=="Present":
            count+=1
    rows[i].append(count)

# finalnamelist.csv fully updated upto now

for i in range(len(rows)):
    print(rows[i])

with open("finalnamelist.csv","w",newline="") as file:
    csvwriter=csv.writer(file)
    for i in range(len(rows)):
        csvwriter.writerow(rows[i])

#fully updated








