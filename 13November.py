#File Handling

'''
file handling demo
'''
#Read m file k exist hona zaruri hai nhi toh error dega
#fp= open("Backup.txt","r+") #yah address deta hai, yeh current directory m check krega
fp= open("Backup.txt","w")
print(fp.name,fp.mode,fp.closed,fp.encoding,sep=" ") #print(fp) fp mtlb files k attributes batayega ... yeh saare attributes  <<---
fp.close() #fp ko close krna zaruri hai
print(fp.closed)

#write mode: overwrites after 1 type typing message
'''
file handling demo
'''

fp= open("Backup.txt","w")

msg=input("Enter your message:")
print(msg)
fp.write(msg)
fp.close()

#append mode
'''
file handling demo
'''
fp= open("Backup.txt","a")
msg=input("Enter your message:")
print(msg)
fp.write(msg+"\n")
fp.close()

# Sum of 2 numbers:
'''
file handling demo
'''

fp=open("output.txt","a")
num1,num2=map(int,input("Enter 2 numbers separated by space:").split())
res=num1+num2
result= f"Sum of {num1} and {num2} ={res}\n"
print(result)
fp.write(result)
fp.close()


'''
file handling demo
'''
#use writelines for collection of strings as (write) mode only accepts string object, nothing other than that , so we use writelines
fp=open("output.txt","a")
lst=["noida ,","dehradun ,","jammu ,","roorkee ,"," Delhi"]
fp.writelines(lst) # can only accept string object, nothing another tahn that
fp.close()


'''
file handling demo
'''
#use writelines for collection of strings as (write) mode only accepts string object, nothing other than that , so we use writelines
fp=open("Backup.txt","r")
text=fp.read() #character by character RAM m store kr dega yeh aur store kr do text m for multiple time access
print(text)
fp.close()

# for reading 2 times from a file
'''
file handling demo'''
import os
os.system("cls")
fp=open("backup.txt","r")
print(fp.read())
fp.seek(0)
print(fp.read())
fp.close()

#for specific reading from a file
#use readline

'''
file handling demo'''
import os
os.system("cls")
fp=open("backup.txt","r")

for i in range(5):
    print(fp.readline() ,end="") #print uses by default \n at the end
fp.close()

#readlines to raed your whole file in a list.

'''
file handling demo'''
import os
os.system("cls")
fp=open("backup.txt","r")

lst=fp.readlines()
for line in lst:
    print(line,end="")

fp.close()


'''
file handling demo'''
import os
os.system("cls")
fp=open("backup.txt","r")

for line in fp.readlines() [::-1]:
    print(line,end="")

fp.close()

#palindrome checking:
import os
'''
file handling demo'''
os.system("cls")
fp=open("output1.txt","r")

for line in fp.readlines():
    line=line.strip("\n")
    if line==line[ ::-1]:
        print(line,"is palindrome !")
    else:
        print(line,"is not palindrome !" )

fp.close()

#simultaneous read and write from and to the file respectively : copy of a file

'''
file copy demo'''

fpr= open("backup.txt","r")
fpw= open("copy.txt","w")

for line in fpr.readlines():
    fpw.write(line)

fpw.close()
fpw.close()

print("File copied successfully....")

#for image data: copying an image

'''
file copy demo'''

fpr= open( "C:\\Users\\DELL\\Pictures\\Screenshots\\code2 sc 7.png","rb")
fpw= open("code.png","wb")

for line in fpr.readlines():
    fpw.write(line)

fpw.close()
fpw.close()

print("File copied successfully....")




