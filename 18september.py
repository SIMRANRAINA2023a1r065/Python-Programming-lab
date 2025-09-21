##string functions
print(dir(str)) ## gives methods available in str(string) class
st="welcome to the world of string !"
st=st.upper() ## variable m store krna pdega, becoz string is immutable
st=st.lower()
## captalize function used to making 1st letter of any word capital
st=st.capitalize()
##title function is used to make 1st letter of every word capital
st=st.title()
## capital ko small aur small ko capital letter m convert krne k liye
st=st.swapcase()
## formatting functions : for left alignment and right alignment of words
name="simran"
age=19
## ist way
##print("my name is ", name," and i am",  age ,"year`s old")
##2nd way
##print("my name is "+name+" and i am "+str(age)+" year`s old")
## print function in python
##print("my name is %s and i am %d year`s old"%(name,age))
## if not using %s,%d , then use this format function
##print("my name is {} and i am {} year`s old".format(name,age)) ## {}--> place holder se yeh fn khudi variables ki value le lega
## * --> vararch : variable length argumnet string ,,,*emp-->this is unpacking of emp list which will automatically access the variables in list
emp=[101,"james","james@gmail.com",10]
print("eid:{} name:{} email:{} did:{}".format(*emp)) ##--> yeh use karo
## f yha yeh batata hai ki jo placeholder m hai voh variable hai yaha
print(f"my name is {name} and i am {age} year`s old") ##--> yeh use karo

headings=["eid","name","email","salary","did"]
emp1=[101,"james","james@gmail.com",6000,10]
##print("{} {} {} {} {}".format(*headings))
## < : left justification and >: right justification
print("{:<7}{:<15}{:<20}{:<9}{:<4}".format(*headings))
print("-"*60)
print("{:<7}{:<15}{:<20}{:<9}{:<4}".format(*emp1))

## to keep the word at the center use center function
st="welcome simran !"
print(st.center(40))
st="15000$"
print(st.ljust(40,'-'))
print(st.center(40,'-'))
print(st.rjust(40,'-'))
 ## encode function: to convert string into binary
st="PYTHON"
##UTF: universal test format
##st="PYTH"+"\u229a"+"N"
print(st) ## it gives circle ring operator
bst=st.encode(encoding="ascii",errors="strict")
print(bst)
## to decode it: jisse vapis PYTHON milega jo original string hai
newst=bst.decode(encoding="ascii",errors="strict")
print(newst)

##UTF: universal test format
st="PYTH"+"\u229a"+"N"
print(st) ## it gives circle ring operator
bst=st.encode(encoding="ascii",errors="ignore")
print(bst)
## to decode it: jisse vapis PYTHON milega jo original string hai
##newst=bst.decode(encoding="ascii",errors="strict")
##print(newst)

st="PYTH"+"\u229a"+"N"
print(st) ## it gives circle ring operator
bst=st.encode(encoding="ascii",errors="replace")
print(bst)
## to decode it: jisse vapis PYTHON milega jo original string hai
##newst=bst.decode(encoding="ascii",errors="strict")
##print(newst)
st="PYTH"+"\u229a"+"N"
print(st) ## it gives circle ring operator
bst=st.encode(encoding="ascii",errors="namereplace")
print(bst)
## strict, replace, ignore, namereplace are errors parameters


## for encryption : use hash lib , use uska function:md5

pwd="simran@123"
import hashlib
encstr=hashlib.md5(pwd.encode())
## encrypted string nikalke dega hashlib object se fir md5 fn se
print(encstr.hexdigest())

# pwd="475fdf947ed49081e754aac4a5357f59"
#import hashlib
#password=input()
st="mississippi"
print(st.count("iss"))

# by using range 
st="mississippi"
print(st.count("s",4,8))

st="mississippi"
print(st.index("p"))


## hiding / masking of a string
st="python i a high level language"
st1="aeiou"
st2="12345"
# transition table / mapping table
ttab=str.maketrans(st1,st2)
print(ttab)
print(st.translate(ttab))


