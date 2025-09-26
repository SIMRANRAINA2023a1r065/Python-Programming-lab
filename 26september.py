#reverse function
lst=["james","neena","blake","neena","anna"]
print(f"Before Reverse:{lst}")
lst.reverse()
print(f"After Reverse: {lst}")

#reversed function
lst=["james","neena","blake","neena","anna"]
print(f"Before Reverse:{lst}")
#lst.reverse()
result=list(reversed(lst))
print(f" Reversed List: {result}")
print(f"After Reverse: {lst}")

#for different types of objects
lst1=[10,[100]]
lst2=lst1 # interning , only one list object is there
print(lst1,lst2)
print(id(lst1),id(lst2))

lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)

# shallow copying
lst1=[10,[100]]
lst2=lst1.copy()
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)
