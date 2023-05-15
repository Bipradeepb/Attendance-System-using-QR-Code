import os
import csv
import base64
from MyQR import myqr

print("Hello World")
#Create the directory where qr codes will be saved

cwd=os.getcwd()
directory="qrcodes"
path=os.path.join(cwd,directory)
print(path)
if not os.path.exits(path):
    os.makedirs(path)

#Start generating the qrcodes
with open("finalnamelist.csv","r",newline="") as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader)
    #take the lines in the file 
    #encode the enrollment number
    for line in csvreader:
        data=str(line[1]).encode('utf-8')
        #print(data)
        id=str(base64.b64encode(data).decode())
        #print(id)

        version,level,qr_name=myqr.run(
            str(id),
            version=1,
            level='H',
            picture="background.png",
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=str(line[0]+".bmp"),
            save_dir=path
        )
    #end of file reading and generating qrcodes
#end of file
    
