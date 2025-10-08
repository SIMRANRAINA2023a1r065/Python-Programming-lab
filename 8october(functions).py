#chp 4:Functions And Modules
# function: It is a tool which is used for performing a particular task, which makes our task more easy.
# It is a set of instructions that is used to perfrom a particular task.
# A function is a set of instructions that is used to perform a single related operations.
# functions are:
#  1. organised
#  2. Re-usable
#  3. Modularized
# Python has many built-in functions like: print(),input(),int(),len().Etc but you can also create your own functions.
# These functions are called user-defined function.
#syntax:
# def <function_name>(parameter1,paarameter2,.....,parameter): , parameter list is optional here
# By default return statement give "None", if you don`t give any return statement in your code.`
#      statement 1
#      statement 2
#      return [expression]

# Standard Library:
# Standard Library is a collection of tools that comes with python. The standard library includes the following:
#---> Built-in Functions (e.g; tool inside taht toolbox) (Functions)
# ---> Modules(e.g; toolbox) (files)
# ---> Packages(e.g; storeroom) (Folders)

#There are many tools available in Python`s Libraries which are developed.
# # duc typing
# def myfunc(st): ---> start of the function
#    print(st) 
#     return st ----> End of the function
# myfunc(st) ---> function calling

def sum():
    i,j=map(int,input("Enter 2 nums:").split(" "))
    print("sum:",i+j)
sum()

#list se bhi kr skte hai

# def add():
#     i=list(map(int,input("Enter  nums:").split(" ")))
#     print(add(i))
# add()
# if you have to take input in string
# i=list(map(int,input("Enter Numbers:").split(" ")))
# i=list(map(int,list)) # es list m hr kisi ko integer m badlega
# print(i)

# agr u have to take input in basis of , and different types of inputs and if separated by " " use map
l,n,s=eval(input())
print(l,n,s,sep="\n")


