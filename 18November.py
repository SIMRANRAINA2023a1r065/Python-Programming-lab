# 13 Lab experiment
# WAP that inputs a text file. The program should print all of the unique words in the file in the alphabatical order.
'''
Exp 13
'''

import os

fname=input("Enter file name:")

f=open(fname,"w+") # Cursor at the begining of the file # opening file in writing mode
msg=input("Enter your message:")
f.write(msg)
print("Data written successfully in file ...")
input("Press any key to continue:")
os.system("cls")
f.seek(0)
string=f.read()
# internally list m convert ho raha hai throught sorted .... kyuki sort nhi chlta unordered collection pe jaise : set
res=sorted(set(string.split(" "))) #set conversion function : for removing duplicasy
for word in res:
    print(word,end=" ")

f.close()

#14 : create a text file"My file.txt" in python and ask the user to write separate 3 lines with three input statements from the user.

'''
  Exp 14
'''

import os
fname=input("Enter file name:")
f=open(fname,"w+")
count=int(input("Enter no. of lines: "))
for i in range(count):
    msg=input()+"\n"
    f.write(msg)

print("Data written successfully in file ...")
input("Press any key to continue:")
os.system("cls")
f.seek(0)
print(f.read())
f.close()

# 9th Lab Exp. 

import os
class Department:
    def __init__(self,did,dname,location):
        self.did=did
        self.dname=dname
        self.location=location #constructor channing 

    def __str__(self):
        return f'{self.did} {self.dname} {self.location}'
    
class Employee:
    def __init__(self,eid,name,department):
        self.eid=eid
        self.name=name
        self.department=department

class DailyWageEmp(Employee):
    def __init__(self,eid,name,dw,nod,department):
        super().__init__(eid,name,department)
        self.dw=DailyWageEmp
        self.nod=nod
        self.salary=self.dw*self.nod
        self.etype="Daily Wage" #extra variable mein value dedi.

    def updateSalary(self,newsal):
        self.dw=newsal #dw ka newsal ho jaygea salary.
        self.salary=self.dw*self.nod
    
    def __str__(self):
        return f'{self.eid} {self.name} {self.salary} {self.etype} {self.department}'
    
class RegularEmp(Employee):
    def __init__(self,eid,name,hra,basic,department):
        super().__init__(eid,name,department)
        self.hra=hra
        self.basic=basic
        self.salary=self.hra+self.basic
        self.etype="Regular"

    def updateSalary(self,newsal):
        self.basic=newsal
        self.salary=self.hra+self.basic

    def __str__(self):
        return f'{self.eid} {self.name} {self.salary} {self.etype} {self.department}'
    
db=[] #database in which employee records will be there.

while(True):
    os.system("cls")
    choice=int(input('''
    1.Insert Employee
    2. Update Salary
    3. Delete Employee
    4. Search Employee
    5. Show all Employees
    6. Show all Departments
    7. Exit
    Enter your choice:- '''))
        
    if(choice==1):
            emp=None
            ch=int(input("1:Regular Employee 2:Daily Wage Employee"))
            eid=int(input("Enter Eid: "))
            name=input("Enter Name: ")
            did=input("Enter Did: ")
            dname=input("Enter Dname: ")
            loc=input("Enter Locartion: ")

            if ch==1:
                basic=int(input("Enter Basic: "))
                hra= int(input("Enter HRA: "))
                emp=RegularEmp(eid,name,hra,basic,Department(did,dname,loc))

            elif ch==2:
                dw=int(input("Enter Daily Wage: "))
                nod=int(input("Enter Number of working days: "))
                emp=RegularEmp(eid,name,dw,nod,Department(did,dname,loc))

            db.append(emp)
            input("press any key to continue")

    elif choice==2:
            eeid=int(input("Enter eid: "))
            amt=int(input("Enter updated amount"))
            for i in range(len(db)):
                if db[i].etype=="Regular":
                    db[i].basic=amt
                else:
                    db[i].dw=amt
            input("press any key to continue")

    elif choice==3:
        eid=int(input("Enter eid: "))
        for i in range(len (db)):
            if db[i].eid==eid:
                del(db[i])
                break
        input("press any key to continue")

    elif choice==4: #Search ke liye: 
        eid=int(input("Enter eid"))
        for i in range(len(db)):
            if db[i].eid==eid:
                print(db[i]) # i is index here.
                break
        input("press any key to coninue")

    elif choice==5:
        for i in db:
            print(i)
        input("press any key to continue")

    elif choice==6:
        for i in db:
            print(i.department)
        input("press any key to continue")
    
    elif choice==7:
        break
    else:
        print("invalid choice")
        input("press any key to continue")

      





         


            







    

