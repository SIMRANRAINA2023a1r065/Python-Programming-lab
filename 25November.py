'''Common Exception Errors:
IO ERROR: if the file cannot be opened.
Import Error: If python cannot find the module.
Value Error: Riased when a built-in operation or function recieves an argument that has the right type but an inappropriate value.
Keyboard Interrupt: Raised when the user hits the interrupt key (normally ctrl+c or delete.)
EOF ERROR: Raised when one of the built-in functions (input() or raw input()  hits an )


'''''' WHERE EXCEPTION MAY OCCUR ?

HARDWARE/OPERATING SYSTEM LEVEL:
1.Arithemtic exceptions; divide by 0, under/overflow.
2.Memory access voilations, stack over/underflow.

LANGUAGE LEVEL:
1.Bounds voilations: illegal indices. eg: list mein 5 index ha aur 10 index pe roor ayega 
2.Value Error: invalid literal, improper casts. int ki jaga string dedi too

PROGRAM LEVEL:
1.User defined exceptions.  :- jo python ki nazar mein nhi hmari nazar mein exception ho.''' 

def division():
    print("inside div function")
    try:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        res=num1//num2
        print(f"division of {num1}//{num2}={res}")
    except (ZeroDivisionError, ValueError) as ob:
        print(ob)
    except Exception as ob:
        print(ob)
    print("end of div function")

print("inside main")
division()
print("end of main")


#oputput file mein jaye aur error aye too vo bhi file mein jaye exception print in file:
def division():
    fp=open("backup.txt","a")
    print("inside div function")
    try:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        res=num1//num2
        msg=f"division of {num1}//{num2}={res}\n"
        print(msg)
        fp.write(msg)
        fp.close()
    except (ZeroDivisionError, ValueError) as ob:
        print(ob)
        fp.write(str(ob)+"\n") #ob ko file meim write krne ke liye convert it into string.
    except Exception as ob:
        print(ob)
    print("end of div function")

print("inside main")
division()
print("end of main")  #try except mutually chlte ha dono ikhatte nhi chlte ya too ek pura chelga ya dusra.


# file ko close krna jaruri pr exception ki waja se file close nhi hui

# finally block har baar chlta ha chahe exception aye ya na aye : resource freeing section 
def division():
    fp=open("backup.txt","a")
    print("inside div function")
    try:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        res=num1//num2
        msg=f"division of {num1}//{num2}={res}\n"
        print(msg)
        fp.write(msg)
        
    except (ZeroDivisionError, ValueError) as ob:
        print(ob)
        fp.write(str(ob)+"\n")
    except Exception as ob:
        print(ob)
        fp.write(str(ob)+"\n")
    finally:
        fp.close()
    print("end of div function")

print("inside main")
division()
print("end of main")

####
def division():
    fp=None
    print("inside div function")
    try:
        fp=open("backup.txt","a")
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        res=num1//num2
        msg=f"division of {num1}//{num2}={res}\n"
        print(msg)
        fp.write(msg)
        
    except (ZeroDivisionError, ValueError) as ob:
        print(ob)
        fp.write(str(ob)+"\n")
    except Exception as ob:
        print(ob)
        fp.write(str(ob)+"\n")
        print("end of div function")
    finally: #resource ko free krne ke liye it is used. beacuse try block complete nhi chlta aur dusra bhi hamesha yhi chlta ha.
        if fp: #agr file ka address ha koi exist krta ha too: fp.close()
            fp.close()
        

print("inside main")
division()
print("end of main")


#uses of else:
print("inside div function")
while True:
    try:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        res=num1//num2
        msg=f"division of {num1}//{num2}={res}\n"
        print(msg)
        
    except (ZeroDivisionError, ValueError) as ob:
        print(ob)
        
    except Exception as ob:
        print(ob)
      
        print("end of div function")
    else:
        print("exception nhi ayi too break!! hua yha else code chlta ha jb excepton na ho")
        break #agr try block mein exception na aye too yeh chlta ha else block : yha exceptuon nhi hogi too break
    finally:
        print("cleanup code")


##
fp=None
try:
    fp=open("ksg.txt","r") #file bani na ho too exception ayega yha , try block ka code clean and tidy.
    # print(fp.read()) code kam hona chiye yha too asani hogi.
    # fp.close()
except FileNotFoundError as ob:
    print(ob)
else:
    print(fp.read())
    print("file found!!")
finally:
    if fp: #agrfile ha too close.
        fp.close()


#raise:
#custom exceptions:-
#citeria age 18 tk hogi, too thik nhi too hault.
def req(age:int)->None:
    if age<18: #python mien this is not an exception but we want yha exception raise ho so use raise here.
        # pass
        raise ZeroDivisionError("You are below age") #this is the constructor of zerodivisionerror class and parameter is Your are below age
    elif age>40:
        # pass
        raise ValueError("You are Above age")
    else:
        print("submit your CV")

req(int(input("enter your age: "))) #ZeroDivisionError: Your are below age yeh hamri marji ka error ha

#how to do exception handling here : of above code:
def req(age:int)->None:
    try:
        if age<18: #python mien this is not an exception but we want yha exception raise ho so use raise here.
            # pass
            raise ZeroDivisionError("You are below age") #this is the constructor of zerodivisionerror class and parameter is Your are below age
        elif age>40:
            # pass
            raise ValueError("You are Above age")
        else:
            print("submit your CV")
    except ZeroDivisionError as ob:
        print(ob)
    except ValueError as ob:
        print(ob)


req(int(input("enter your age: ")))


#--------------------CUSTOM EXCEPTIONS:----------------------------------------------------------------------------#
#----------how to make custom exception:  using oops:
class BelowAgeException(Exception):
    #exception se "inherit" krna pdta ha custom class ko,so custom class behaves as exception : #parent is base exception of exception.
    def __init__(self,msg): #constructor 
        self.msg=msg

    def __str__(self): # string method : magic fn
        return self.msg
    
    def __del__(self): # destructor: magic fn
        print("object destroyed")
     
     
class AboveAgeError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):   #object ko print krna ha too object ko string mein print krege
        return self.msg
    
    def __del__(self): # destructor: magic fn
        print("object destroyed")

def req(age:int)->None:
    try:
        if age<18: #python mien this is not an exception but we want yha exception raise ho so use raise here.
            # pass
            raise BelowAgeException("You are below age") #this is the constructor of zerodivisionerror class and parameter is Your are below age
        elif age>40:
            # pass
            raise AboveAgeError("You are Above age")
        else:
            print("submit your CV")
    except BelowAgeException as ob:
        print(ob)
    except AboveAgeError as ob:
        print(ob)
    except Exception as ob:  #koi aur exception na ajaye too, tbhi exception bhi dedi
        print(ob)

req(int(input("enter your age: ")))