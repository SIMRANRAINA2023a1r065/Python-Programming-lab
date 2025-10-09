#Python supports call by value(where the value is always an object reference, not the value of the object )
# Hence, many professionals term it as Pass by Object reference
#pass/call by object reference in python , a method of function making

lst=[10,20,30]
lst2 = lst
print(lst2 is lst)

lst=[10,20,30]
lst2 = lst.copy()
print(lst2 is lst)

lst="jame"
lst2=lst
print(lst2 is lst)

#string is immutable
lst="jame"
lst2=lst
print(lst2 is lst)
lst=lst+"bond"

#print(lst) --> prints "jamesbond"
print(lst2) # --> prints "james"

#function m function k references pass hote hai
#Argument passing mechanism in functions
lst=["MIET"]
def test(p):
    p.append("Jammu")
print(lst)
test(lst)
print(lst)

#string mutable hai toh original string m koe change nhi hoga 
lst="MIET"
def test(p):
    p=p+"jammu"
print(lst)
test(lst)
print(lst)
#yaha hmmne naya list diya hai test(p) m toh voh list m change reflect hua
lst=["MIET"]
def test(p):
    p=["Jammu"]
print(lst)
test(lst)
print(lst)

#scopes: local variable, global variable, tells accessibilty and life of a scope
#The variable defined within the function has a local scope and are called local variables.
#they can be accessed with that particular function only.
#They 
#scopes:
#local
#built-in
#global (module level value)
#inclosing

#scopes understanding:
#parent() is a enclosing block of lcl()

#built-in scope
num=10 #---> global scope
def parent():
    num=100  #---> enclosing scope
    def lcl():
        num=1000
        print(num)#--> local scope

num=10

def test():
    num=100
    print(num)
test()
print(num)

num=100

def test():
    global num # use global keyword to modify it
    num+=100
    print(num) #you can`t modify the global variable, you can access it only .
test()
print(num)

def fun2():
    z=30
    print("Inside fun2:")
def fun1():
    y=20
    print("Inside fun1:")
    fun2()
    print("end of fun1:")

print("inside main:")
fun1()
print("End of main !")

#type of function parameter
#parameters: voh jo calling environment se milta hai

#1.mandatory positional arguments (critical)
#2. optional argument
#3. Var argument
#4. Key var argument
#5. Keyword
def  printname(fname):
    print(f"fname:{fname}")

printname("simran")
#1.) Required positional argument
def  printname(fname):
    print(f"fname:{fname}")

printname() #---> error aayega , becoz here argument is mandatory

#Type hinting: for making your program readale
def  printname(fname:str) ->None: #---. type hinting is optional
    print(f"fname:{fname}")

printname(100)
#type hinting m agr aapne string diya toh usse k sare funtions aapko dega
# def  printname(fname:str) ->None: #---. type hinting is optional
#     fname.()

def printname(fname,lname):
    print(f"fname: {fname} lname:{lname}")
printname("simran","Raina")

#2)optional/default argument
def printname(fname,lname="Na"):
    print(f"fname: {fname} lname:{lname}")
printname("simran") # --> agr lname nhi denge toh "Na" hoga

# def printname(fname="na",lname): ---> error dega
#     print(f"fname: {fname} lname:{lname}")
# printname("simran")

#function overloading
def add(num1,num2):
    return num1+num2
def add(num1,num2,num3=0): # yha optional parameter use karo
    return num1+num2+num3
def add(num1,num2,num3=0,num4=0):
    return num1+num2+num3+num4
print (add(1,2))

def printname(fname,mname="Na",lname="Na"):
    print(f"fname: {fname} mname={mname} lname:{lname}")
printname("simran") 

#keyword argument
#used for skipping middle name
def printname(fname,mname="Na",lname="Na"):
    print(f"fname: {fname} mname={mname} lname:{lname}")
printname("simran",lname="Raina") 

def printname(fname,mname="Na",lname="Na"):
    print(f"fname: {fname} mname={mname} lname:{lname}")
printname(mname="shhhhh",lname="Raina",fname="simran") 

#parameter m starting m keyword argument de diya toh saare baaki arguments bhi keyword argument se hi dena  pdega

def printname(fname,mname="Na",lname="Na"):
    print(f"fname: {fname} mname={mname} lname:{lname}")
printname("james",mname="shhhhh",lname="Raina",fname="simran") #--. multiple values argument error ayega





