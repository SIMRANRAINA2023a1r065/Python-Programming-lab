"""
Pattern printing
*
* *
* * *
* *  * *


for i in range(1,6):
    for j in range(i):
        print("* ",end="")
    print()
    

for i in range(1,6):
    for j in range(i):
        print(i," ",end="")
    print()
    

for i in range(1,6):
    for j in range(i):
        print(j+1," ",end="")
    print()
    
  
for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print("0"," ",end="")
        else:
            print("1"," ",end="")
    print()
    
counter =1
for i in range(1,6):
    for j in range(i):
        print(counter," ",end="")
        counter+=1
    print()

###flautz triangle
counter =65
for i in range(1,6):
    for j in range(i):
        print(chr(counter)," ",end="")
        counter+=1
    print()
    
print("'simran'")
print('\'simran\'')

st='''welcome
to
the
world
of
string '''
##print(st)

str="hello"
str(12)
'12'
str("12")
'12'
str('12')
'12'
st="hello"
st
'hello'
st+="simran"
st
'hellosimran'
id(st)
2490412646000
st="hello"
id(st)
2490376078800
st+="simran"
st
'hellosimran'
id(st)
2490370356464
st="hello"
st2=st
st2+="world"
st2
'helloworld'
st
'hello'
id(st)
2490376078800
id(st2)
2490370034160
st="python"
st
'python'
st[0]
'p'
st[len(st)-1]
'n'
string object does not support deletion and updation,insertion

st="python"
print(st[0],st[-6])
print(st[0:4])
pyth
print(st[0:3])
pyt
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy
print(st[2:6])
thon
print(st[2:])
thon
print(st[:])
python
print(str[::2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(str[::2])
TypeError: type 'str' is not subscriptable
print(st[::2])
pto
print(st[1::2])
yhn
print(st[::-1])
nohtyp
print(st[::-2])
nhy

"""
##palindrome code
st=input("Enter a string")
if st==st[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


