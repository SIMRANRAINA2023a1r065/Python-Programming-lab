stulist=[]
num=int(input("Enter number of students:"))
for i in range(num):
    d={}
    rno=int(input("Enter Roll No:"))
    name=input("Enter Name:")
    year=input("Enter year/section:")
    email=input("Enter Email:")
    dept=input("Enter dept:")
    d={"rno":rno,"name":name,"Year":year,"email":email,"dept":dept}
    stulist.append(d)

for i in stulist:
    print(i)

#Search by roll number
search_rno = int(input("\nEnter roll number to search: "))
for s in stulist:
    if s["rno"] == search_rno:
        print("Roll No:", s["rno"])
        print("Name   :", s["name"])
        print("Year :", s["Year"])
        print("Email  :", s["email"])
        print("Dept   :", s["dept"])
        break
else:
    print("No student found with Roll No:", search_rno)