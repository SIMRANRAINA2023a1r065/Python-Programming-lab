#constructor:__init__ --> known as magic fn : which starts with double underscore
class Student:
    def __init__(self,rollno,name,per):
        self.rollno=rollno
        self.name=name
        self.per=per
    def __str__(self):  # it returns string object in proper format
        return f'''
        rollno:{self.rollno} name:{self.name} per:{self.per:0.2f}
        '''
stu=Student(101,"king",99.999)
print(stu) # when printing object on calling it, it gives address of that object
# for proper format

#12th Lab Experimemt: Write a program to armstrong:

def max_of_three(num1:int,num2:int,num3:int)->bool:
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
        
num1,num2,num3=map(int,input("Enter 3 numbers separated by space:").split())
maxnum=max_of_three(num1,num2,num3)
print(f"Maximum of 3 numbers are:{maxnum}")
#Armstrong Number
# 123= 1**3 +2**3 +3**3
# 153= 1**3 + 5**3 +3**3 # it is a armstrong number (power m no. of digits aata hai)
#1-9: by default armstrong number hote hai

def countdigit(num):
    c=0
    while(num>0):
        c+=1
        num=num//10 
    return c
        

def CheckForArmstrong(num:int)->bool: # 153
    count=countdigit(num)
    sumofnum=0
    for digit in str(num):
        sumofnum+=int(digit)**count
    if sumofnum==num:
        return True
    else:
        return False
    
num=int(input("Enter a number to check for armstrong:"))
if(CheckForArmstrong(num)):
    print(f"{num }is an narmstrong number !")
else:
    print(f"{num} is not an armstrong number !")


#Exp 9: Employee Management system :classes #Aggregiation /composition
#Write a program to implement Employee Managemenet System (EMS): oobject ki nesting 
#Aggregation / Composition
class Address:
    def __init__(self,street,city,state,pin):
        self.street=street
        self.city=city
        self.state=state
        self.pin=pin
    
    def __str__(self): #" magic fn"  name is __str__: else it gives error  -> operator overloading
        #__str__ is permanaent , we can't change it, it's predefined
        return f"\nAddress:{self.street} {self.city} {self.state} {self.pin}" 
    
# add=Address("street no-7","noida","up","378732")
# print(add) #add retruns str and then that str will print

#Department has an address / Department composed of address.
class Department:
    def __init__(self,did,dname,address):
        self.did=did # int composition
        self.dname=dname # string composition
        self.address=address # user defined composition
    
    def __str__(self):
        return f"\nDepartment did:{self.did} dname: {self.dname} {self.address}"


# dept=Department(10,"IT",Address("street no-7","noida","up","378732")) #Anynomous object here is Address having no name, yhi pe sue , yhi pe beanga for one time usage
# # run time pe upar wala class consider hoga for 
# print(dept)

#Inheritance:
#department assign hoga employee ko

class Employee:
    def __init__(self,eid,name,dept):
        self.eid=eid
        self.name=name
        self.dept=dept

    def __str__(self):
        return f"\nEmployee eid: {self.eid} name: {self.name} {self.dept}"
    
class RegEmp(Employee):
    def __init__(self,eid,name,basic,hra,dept):
        super().__init__(eid,name,dept)
        self.basic=basic
        self.hra=hra
        self.salary=self.hra+self.basic
    
    def __str__(self):
        return f"{self.eid} {self.name} {self.dept}"
    
class DwEmp(Employee):
    def __init__(self,eid,name,dw,nod,dept):
        super().__init__(eid,name,dept)
        self.dw=dw
        self.nod=nod
        self.salary=self.dw*self.nod

    def __str__(self):
        return f"{self.eid} {self.name} {self.salary} {self.dept}"

reg=RegEmp(101,"james",40000,12000,Department(10,"IT",Address("street no-7","noida","up","378732")))
print(reg)

dwemp=DwEmp(102,"King",500,22,
            Department(10,"IT",
                       Address("street no-7","noida","up","378732")))
print(dwemp)


