# print("hello")
# st="hello"
# print(st,id(st))
# ## hello: l ek hi object se reference lega eseliye object id smae aa rha hai l ka dono baari
# for i in st:
#     print(i,id(i))

# st="misssissippi"
# print(st,id(st))
# ## hello: l ek hi object se reference lega eseliye object id smae aa rha hai l ka dono baari
# ## That`s how it saves memory by giving same reference to same object
# for i in st:
#     print(i,id(i))

##slicing
# st="welcome"  
# print(st[::-2])
# st="welcome"  
# print(st[::2])

## we have to swap 1st 2 characters  with last 2 charcters and last 2 characters with 1st 2 characters
## output:welcome --->> melcowe
# st=input("Enter a string")
# if(len(st)>=4):
#   print(st[-2:]+st[2:-2]+st[:2]) ## view banata hai

## u have to st="abracadabra" -->>"abr$c$d$br$"
# st="abracadabra"
# s=st[0] ## yeh pehla character dala: a
# for i in st[1:]: ## yah vala loop b se end tk chl raha hai
#     if i ==st[0]: ## if character ==a
#         s+='$'
#     else:
#         s+=i
# print(s) ## new string jo bni hai voh print hogi 
## convert uppercase to lowercase
##st="SIMRAN" -->"simran"
st=input("Enter a string:")
print(st.lower())


