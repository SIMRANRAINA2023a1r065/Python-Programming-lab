#select* from emp1.txt
import os
os.system("cls")
empfp =open("emp1.txt","r")

#For reading purpose

for record in empfp.readlines():
    print(record.split(",")[-1].rstrip("\n"))
    #split ek list return krta hai


# select* from emp1.txt where did=50/any did

import os
os.system("cls")
empfp =open("emp1.txt","r")

#For reading purpose
did=input("Enter did:")
for record in empfp.readlines():
    if did ==record.split(",")[-1].rstrip("\n"):
        print(record,end="")
    #split ek list return krta hai

#jinko commision milti hai voh employees nikalo
import os
os.system("cls")
empfp =open("emp1.txt","r")
for record in empfp.readlines():
    if record.split(",")[-3].rstrip("\n") != 'NULL':
        if record.split(",")[-1].rstrip("\n"):
          print(record,end="")