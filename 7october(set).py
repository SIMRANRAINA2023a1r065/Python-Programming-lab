#set properties
#to remove duplicacy, we use set... It is un-ordered collection
#a)It is not a sequence(indexing and slicing are not allowed).
#b)It is mutable(operations like insertion and deletion are allowed).
#c)It is an un-ordered collection.
#d)It can not contain duplicate elements.
#e) It can`t preserve the insertion order.
#f) It may contains only immutable type of obj.

#st=set("any obj") # To convert any type of obj into a set
st=set("MISSISSIPPI")
print(st)
st=set(['M','I'])
print(st)

st={"james","simran","payal","mahi"}
print(st)
st=set() # set khali ase hi aayega , aur kse nhi
print(type(st))

st={}
print(type(st))#dict dega


st1={"red","blue"}
st2={"blue","red"}
print(st1==st2)
     
st=set()
st.add(10)
print(st,id(st))
st.add(20)
print(st,id(st))
st.add(30)  #set is mutable
print(st,id(st))
st.remove(30)
print(st,id(st))
#updation nhi hoga kyuki uske liye indexing pta honi chaihaye voh hme allowed nhi hai yaha
#hashing : sirf immutable ko deta hai, mutable pe hi dega bs
st=set()
st.add([12,23])

st={12,12.3,12+5j,True,(12,),"james"}
print(st)
fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
newset=fac.union(stu)
print("union:",newset)
# if u want ki sirf change faculty m hi reflect ho ...newset na bne,, overwrite hoga faculty m
fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
fac.update(stu)
print("Union:",fac)

fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
newset=fac.intersection(stu)
print("fac:",fac)
print("stu:",stu)
print("Intersection:",newset)

fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
fac.intersection_update(stu)
print("fac",fac)
#set difference, sirf fac (alg jo ho) aur stu ka bhi same
fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
newset=fac.difference(stu)
print("Intersection:",newset)
newset=stu.difference(fac)
print("Intersection:",newset)

#symmetric difference : non-common elements dega dono m
fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
newset=fac.symmetric_difference(stu)
print("Symmetric Intersection:",newset)

#superset,subset
st1={"red","green","blue"}
st2={"green"}
print(st1.issuperset(st2))
#issubset,issuperset,isdisjoint
st1={"red","green","blue"}
st2={"green"}
print(st2.issubset(st1))
st1={"red"}
st2={"green"}
print(st2.isdisjoint(st1))
#union,intersection,difference,symmetric_sifference: dusra treka
fac={"c","cpp","java","php"}
stu={"js","python","c","cpp"}
print(fac|stu) #union
#ac|=stu
#print(fac)
print(fac&stu) # intersection
# fac&=stu
# print(fac)
print(fac-stu) #set diffrence
print(stu-fac)
print(fac^stu)#symmetric difference
#immutable list=tuple
#immutable set=fronzenset
lst=frozenset(["james","neena","simran"])
print(lst)

a=["james","simran","payal","mahi"]
for i,j in enumerate(a):
    print(i,j)
 #for specific value
a=["james","simran","payal","mahi"]
for i,j in enumerate(a):
    if i==2:
      print(j)
