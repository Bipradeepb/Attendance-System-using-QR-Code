import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import base64
import sys
import time
import datetime
import xlwt
from xlwt import Workbook
import csv
import os

# print("Hello World")

record={}

with open("finalnamelist.csv","r",newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader)

    for line in csvreader:
        record.update({line[1]:[line[0],line[2]]})

#record is stored
#id:[name,gsuite-id]
        
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

fob = open('attendence.txt', 'w+')

names = []

def check(id):
    for i in range(len(names)):
        if(names[i][0]==id):
            return True

    return False


def enterData(z):
    if check(z):
        pass
    else:
        temp=[]
        temp.append(z)
        curtime=datetime.datetime.now().strftime("%H:%M:%S")
        temp.append(str(curtime))
        names.append(temp)
        #append the time
        z = ''.join(str(z))
        fob.write(z + '\n')
    return names


print('Reading...')


def checkData(data):
    try:
        data = str(base64.b64decode(data).decode())
    except(TypeError):
        print('Invalid ID !!!')
        return
    if (check(data)):
        print('Already Present')
    if data not in record:
        print("Invalid Id !!!")
        return
    else:
        print('\n' + str(len(names) + 1) + '\n' + data)
        enterData(data)
    cv2.putText(frame, str(base64.b64decode(obj.data)), (50, 50), font, 2,
                (255, 0, 0), 3)


while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        # print("Data", base64.b64decode(obj.data))
        # enterData(base64.b64decode(obj.data))
        # print(len(names))
        # sys.stdout.write('\r'+'Reading...'+str(len(names))+'\t'+str(base64.b64decode(obj.data)))
        # sys.stdout.flush()
        time.sleep(1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y %I:%M:%S %p")
reg_format_date = reg_format_date.replace(':', ' ')

#write in csv file namelist
#which will store the daily attendance list temp
#also store a backup file in another directory

curdir=os.getcwd()
directory="daily_attendance_details"
path=os.path.join(curdir,directory)

if not os.path.exists(path):
    os.mkdir(path)

curdate=datetime.datetime.now().strftime("%d-%m-%Y")

filename=str((str(curdate))+".csv")
filepath=os.path.join(path,filename)

print(filename)
print(filepath)
print(names)
#create backup

with open(filepath,"w+",newline="") as writefile:
    csvwriter=csv.writer(writefile)
    csvwriter.writerow(["Name","ID","G-Suite Id","Time In"])
    
    for i in range(len(names)):
        lis=[]
        lis.append(record[names[i][0]][0])
        lis.append(names[i][0])
        lis.append(record[names[i][0]][1])
        lis.append(names[i][1])
        csvwriter.writerow(lis)


#update namelist
with open("namelist.csv","w",newline="") as writefile:
    csvwriter=csv.writer(writefile)
    csvwriter.writerow(["Name","ID","G-Suite Id"])

    for i in range(len(names)):
        lis=[]
        lis.append(record[names[i][0]][0])
        lis.append(names[i][0])
        lis.append(record[names[i][0]][1])
        csvwriter.writerow(lis)


# def writeExcel(names, reg_format_date):
#     wb = Workbook()

#     sheet1 = wb.add_sheet('Sheet 1')
#     for i in range(0, len(names)):
#         sheet1.write(i, 1, names[i])

#     wb.save(reg_format_date + '.xls')


# writeExcel(names, reg_format_date)