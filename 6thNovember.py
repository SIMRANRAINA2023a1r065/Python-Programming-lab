#OOPS
#Inheritance: It is a Concept of Code Reusability, refines existing modules and give u a new project or a code
#saves time
#Inheritance is the mechanism of acquiring some attributes of any existing class type into a new class type.
# One of the key concepts of OOPS`s.
#super/parent/base class
#sub/child/derived class
#composition: has a relationship e.g; My car has a music system (not mandatory)
#Inheritance: is a relationship
# Establishes a hierarchical relationship among classes.
#Establishes a superclass/subclass relationship.
#Establishes "is a" relationships. e.g; eye surgeon is a doctor (is not mandatory)
#Benefits:
# Reusability of code.
# Put code in one class, use it in all the subclasses.
# write general purpose code designed for a supertype that works for all subtypes.
# A superclass defines a general set of functionality, whereas subclasses define functionalities specific to them.

 #code: hierarchical inheritance
# class Employee:
#     def  __init__(self,eid,name):
#         self.eid=eid
#         self.name=name
#     def printEmp(self):
#         print(f"eid:{self.eid} name:{self.name}")

# class RegEmployee(Employee): # minimal class; koe data nhi hai bs structure hai unka
#     #pass # function bana liya but usme koe statements nhi hai toh pass use karo
#    def __init__(self,eid,name,basic,hra,da):
#        super().__init__(eid,name)
#        self.basic=basic
#        self.hra=hra
#        self.da=da
#        self.salary=self.basic+self.hra+self.da*30
#    def printRegEmp(self):
#       super().printEmp()
#       print(f"""
#              Basic: {self.basic}
#              HRA: {self.hra}
#              DA: {self.da}
#              Salary:{self.salary}
#              """)
# class DailywageEmployee(Employee):
#     def __init__(self,eid,name,wage,nod):
#         super().__init__(eid,name)
#         self.wage=wage #double underscore: private, double underscore: protected , yah by default public hai
#         self.nod=nod
#         self.salary=self.wage*self.nod

#     def printDWEmp(self):
#             super().printEmp()
#             print(f"""
#                   Daily wage: {self.wage}
#                   Number of days:{self.nod}
#                   salary:{self.salary}
#                   """ )
# obj1=RegEmployee(101,'Simran',200,3000,12)
# obj1.printRegEmp()

# obj2=DailywageEmployee(102,"Payal",800,22)
# obj2.printDWEmp()
        
# # practice code:    Multilevel Inheritance
# # Employee:
# # eid, name,email
# # printEmp()

# # Manager:
# # department
# # printMgr()

# # Director:
# # location
# # printDir()

# # obj=Director()
# class Employee:
#     def __init__(self,eid,ename,email):
#       self.eid=eid
#       self.ename=ename
#       self.email=email
#     def printEmp(self):
#        print(f"eid:{self.eid} ename:{self.ename} email:{self.email}")
# class Manager(Employee):
#    def __init__(self,eid,ename,email,department):
#       super().__init__(eid,ename,email)
#       self.department=department
#    def printMgr(self):
#       super().printEmp()
#       print(f"""
#              Department: {self.department}
#             """)
# class Director(Manager):
#     def __init__(self,eid,ename,email,department,location):
#        super().__init__(eid,ename,email,department)
#        self.location=location
#     def printDir(self):
#        super().printEmp()
#        super().printMgr()
#        print(f"""
#         location: {self.location}
#              """)
# obj1=Director(101,"Simran","xyz@gmail.com","CSE","Jammu")
# obj1.printDir()

#
class Employee:
    def __init__(self,eid,ename,email):
        self.eid=eid
        self.ename=ename
        self.email=email
    
    def EmpDetails(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
Email: {self.email}
""")

class Developer:
    def __init__(self,proglang,workex):
        self.proglang=proglang
        self.workex=workex

    def DeveloperDetails(self):
        print(f"""
programming language: {self.proglang}
Work Experience: {self.workex}
""")


class Manager(Employee,Developer):
    def __init__(self,eid,ename,email,proglang,workex,dept,location):
        Employee.__init__(self,eid,ename,email)
        Developer.__init__(self,proglang,workex)
        self.dept=dept
        self.location=location

    def ManagerDetails(self):
        super().EmpDetails()
        super().DeveloperDetails()
        print(f"""
Department: {self.dept}
Location: {self.location}
""")



obj3=Manager(102,'neena',"fahgda","CPP",12,"CSE","Delhi")
obj3.ManagerDetails()
