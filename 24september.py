#list data structure
#'james' "james" '''james''' """james""" => str
#[12,13,14,12,15] => list
#[12 13 12 14 15] => ndarray
#(12,12,14,15) => tuple
#{12,23,15} => set
# {1:12, 2:56} => dictionary

# 2 different ways to make a list:
# 1) list() -> when we want to convert existing object into list
# 2) [] -> when we want to create a new list object / new list from beginning/ from scratch
# for making / creating empty list object
lst=list()
lst=[]
print(lst,type(lst))

# converting this "hello" string into a list  (1st way ) # bna hua ko convert krna ho
st="HELLO"
lst=list(st)
print(lst) 
# manually converting a string into a list, new list banana ho
lst=['H','E','l','l','o']
print(lst)

# list k andr sirf sequence allowed hai , integers , float, complex , boolean nhi allowed hai
lst=list(12345)
print(lst) # error: int object is not iterable

#    0   1  2  3  4
lst=[10,20,30,40,50]
#    -5 -4 -3  -2 -1
for i in lst:
    print(i,end=" ")
    print(lst[-3:-1])
    #print(lst[-5:])
    print(lst[0::2])
    print(lst[::3])
    print(lst[::-1])
    print(lst[::-2])

#slice[sindex:endindex(this is exclusive, not included)(:step)]
# start : df value=0 , stop : df value = length-1, step: df value =1
# step = -1 , list reverse m access hogi
lst1=[10,20]
lst2=[20,10]  # sequence matters here
#lst2=[20,10]
print(lst1==lst2)
#print(lst1==lst2)
