#Aim: write a program to illustrate iteration over the list and dictionary.
#list definition
#dictionary definition
#loop definition
lst=["c","cpp","c#","js","python"]
print("Elements of list are as:")
for item in lst:
    print(item)

d={"r":"red","g":"green","b":"blue","c":"cyan"}
print("keys of dictionary:")
for key in d.keys():
    print(key,end=" ")

print("\nValues of dictionary:")
for value in d.values():
    print(value,end=" ")

print("\nItems of dictionary:")
for item in d.items():
    print(item,end=" ") # by default tupple dega yeh

# Aim: WAP to reverse every Kth row in a matrix.
lst=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
def reverse(lst,pos):

    for i in range(len(lst)):
        if i== pos-1: # row no yaha position yaha hai
            lst[i]=lst[i][::-1]
print(lst)
reverse(lst,int(input("Enter the row number:")))
print(lst)

#Aim: Create a database using lists and tuples
database=[]
def createdatabase():
    count=int(input("Enter number of students:"))
    for i in range(count):
        sid=int(input("Enter Student Id:"))
        name=input("Enter Student Name:")
        cgpa=float(input("Enter CGPA:"))
        branch=input("Enter Branch Name:")
        email=input("Enter Email:")
        record=(sid,name,cgpa,branch,email)
        database.append(record)

def printdb():
    print("Student Database".center(60,"-")) 
    print(f"{'sid':<10}{'name':<15}{'cgpa':<10}{'branch':<15}{'email':<20}")
    print("".center(70,"-"))
    for record in database:
         print(f"{record[0]:<10}{record[1]:<15}{record[2]:<10}{record[3]:<15}{record[4]:<20}")
    print("".center(70,"-"))
createdatabase()
printdb()   
#print("Developed by ER.Simran Raina")