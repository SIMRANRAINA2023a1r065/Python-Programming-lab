#using simple constructor:

class Student:
    #"""class variable : wich is common for all objects"""
    cname="MIET" #one cname is used by all the objects jo bhhi new object banaega
    def __init__(self):
        self.sid=None #self is used because: 
        self.name=None
        self.branch=None  #by default this is public   #"""""instance variable inside consturctor"""""
        self.sem=None
        self.cgpa=None
        self.email=None #consturctor benagea too set data fn bhi banagea to update 

    # def __init__(self,sid,name,branch,sem,cgpa):  #--paramterized constructor--- ek baar hi chlta ha update ke loye use hota ha fn 
    #     self.sid=sid #self is used because: 
    #     self.name=name
    #     self.branch=branch  #by default this is public
    #     self.sem=sem
    #     self.cgpa=cgpa

    def setData(self,sid,name,branch,sem,cgpa,email): #self ke liye no parameter send 
         self.sid=sid  #object ke andar ka instance member jo none ko overwrite krta ha aur value dalti ha phir ismein.
         self.name=name
         self.branch=branch
         self.sem=sem
         self.cgpa=cgpa
         self.email=email
        
    def updateEmail(self,newemail):
        self.email=newemail #self obj ko baar baar change krega : -------------setter fn used to set the values of instance varaiable 
        # ---------------------------to input getter function.

#to cchage class varaibles make static fn which not insludes self parameter:
    @staticmethod
    def updatecollegename(newcname): #static fn likhoge too no error becuase by default pythonn ko chaiye self
        Student.cname=newcname #both objects cname chnage to newcname
     
    def printDetails(self):
        print(f"""
                  sid: {self.sid}
                  Name: {self.name}
                  Branch: {self.branch}
                  Semester: {self.sem}
                  CGPA: {self.cgpa}
                  email: {self.email}
                  college Name: {Student.cname}""") #self replaced by class name agr self use kroge too automatically replaced 

# Student ob.Student() in c++
ob=Student() #ob is a refernce varaible which is holding propertis of student.
ob.printDetails()

ob1=Student()
ob1.printDetails()
# print(ob.sid," ",ob.name)

ob.setData(101,'james','cse',7,9,'101@jmu.in')
ob1.setData(102,'Neena','IT',3,8,'102@jmu.in')
ob.printDetails()
ob1.printDetails()

ob.updateEmail("neena@xyc.com")
ob.printDetails()

Student.updatecollegename("IITK")
ob.printDetails()
ob1.printDetails()

#instace variable, class variable, instance method, class method 
#self naqme can be anything as it is an identifier but python says to take it as self only.



# ob2=Student()
# print(ob2.__sid," "ob2.__name) for private

# #private:
# self.__sid=None

# #protected:
# self._sid=None

# #------------------parametrized constructor:---------
# def __init__(self,sid,name,branch,sem,cgpa):
#         self.sid=sid #self is used because: 
#         self.name=name
#         self.branch=branch  #by default this is public
#         self.sem=sem
#         self.cgpa=cgpa
# ob3=Student(101,'james','cse',7,9)
# ob3.printDetails()

#--------------"self" is current object reference and in c++ its "This".



# #question: Employees state: eid name sal cname
# #set details()
# getdetails()
# updatedetails()
# updatesal()
# update cname()


# using parametrized constructor:
class Employee:
    cname="Apple"
    def __init__(self,eid,name,sal):  #--paramterized constructor--- ek baar hi chlta ha update ke loye use hota ha fn 
        self.eid=eid #self is used because: 
        self.name=name
        self.sal=sal #by default this is public

    def setDetails(self,eid,name,sal): #self ke liye no parameter send 
         self.eid=eid  #object ke andar ka instance member jo none ko overwrite krta ha aur value dalti ha phir ismein.
         self.name=name
         self.sal=sal
    
    def updateSal(self,newSal):
        self.sal=newSal

    @staticmethod
    def updatecname(newcname): #static fn likhoge too no error becuase by default pythonn ko chaiye self
        Employee.cname=newcname #setter function
    
    def getDetails(self):
        print(f"""
                  eid: {self.eid}
                  Name: {self.name}
                  Sal: {self.sal}
                  college Name: {Employee.cname}""")
        
ob=Employee(101,'James',45000)
ob.getDetails() #getter function

ob1=Employee(102,'Neena',55000)
ob1.getDetails()


ob.updateSal(460002)
ob.getDetails()

Employee.updatecname("Samsung")
ob.getDetails()
ob1.getDetails()

