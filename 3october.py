
#Dictionary methods
d={}
d1={"r":"red"}
d2={"g":"green"}
d.update(d1)
d.update(d2)
print(d)

d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)

#set default fn is used only single value to dictionary
# for avoid overwriting the value if it is already there. kuch nhi hoga...agr nhi ho toh add kr dega
d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)
d.setdefault("g","green")
print(d)
#//2
d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)
d.setdefault("b","blue")
print(d)

#clear fn
d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)
d.setdefault("b","blue")
print(d)
d.clear()
print(d)

# to remove values in dictinary use: popitem():removes last item in dictionary, it returns key:value pair
d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)
d.setdefault("b","blue")
print(d)
#d.clear()
#print(d)
print(d.popitem())
print(d)
#for removing a specific item in dictionary and it returns only value, not key and takes key as parameter
d={}
d1={"r":"red"}
d2={"g":"green"}
for i in d1,d2:
   d.update(i)
print(d)
d.setdefault("b","blue")
print(d)
#d.clear()
#print(d)
# print(d.popitem())
# print(d)
print(d.pop('g'))
print(d)
#for retreiving only keys from dictionary
d={'r':'red','g':'green','b':'blue'}
d2=dict.fromkeys(d,0) # default value of value is 0
print(d2)

#iterating in dictionary
d={'r':'red','g':'green','b':'blue'}
for i in d:
   print(i,d[i]) # i se key aur d[i] se uski value milegi

# for getting only keys, values or puri dictionary
d={'r':'red','g':'green','b':'blue'}
for i in d:
   print(i,d[i])
print(d.keys())
print(d.values())
print(d.items())
#by using unpacking method
for i,j in d.items():
    print(i,j)

#accessing a specific value in dictionary
d={'r':'red','g':'green','b':'blue'}
for i in d:
   print(i,d[i])
print(d.keys())
print(d.values())
print(d.items())
#by using unpacking method
for i,j in d.items():
    print(i,j)
    # for not getting exception error while giving invalid key which is not there in dictionary, so use get fn
print(d.get("g"))
#print(d.get("z"))
print("Important code")

#list question: get length of each name and append it in new list
lst=["simran","payal","mahi","divanshi","ranjeeta","bhawana"]
l=[]
for name in lst:
  l.append(len(name))
print(lst,l,sep="\n")

#append that name which has more than 5 charaters at the end of the list
lst=["simran","payal","mahi","divanshi","ranjeeta","bhawana"]
for name in lst[:]:
   if len(name)<5:
      lst.append(name)
print(lst)

# lst=["simran","payal","mahi","divanshi","ranjeeta","bhawana","mahi"] -> yah o/p ana chaiye