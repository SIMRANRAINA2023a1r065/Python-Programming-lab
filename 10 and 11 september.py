##char=input("Enter the character")
##if len(char) ==1:
##    match char:
##        case 'A':print("Vowel")
##        case 'E':print("Vowel")
##        case 'I':print("vowel")
##        case 'O':print("vowel")
##        case 'U':print("vowel")
##        case _:print("Consonat")
##else:
##    print("Invalid char")
##num=int(input("Enter the number of dow:"))
## case 1:print("Sunday")
## case 2:print("Monday")
## case 3:print("Tuesday")
## case _:print("Invalid choice")
##init=1
##while init<=5 :
##    print(init,"Hello world !")
##    init+=1


##
##while True:
##    print("Hello world")
##    choice=input("do u want to print it again y/n")
##    if choice=='n':
##        break
##

##import random
##num=random.randint(1,100)
##num1=int(input("Enter any number:"))
##if (num1>num):
##    print(num1," is too high than", num)
##else:
##    print(num," is too low than", num1)

import random
num=random.randint(1,100)
c=0
while(True):
    c+=1
    guess=int(input("Enter a number:"))
    if(guess<num):
        print("number too low")
    elif(guess>num):
            print("number too high")
    else:
        break
print("Congratulations You guessed the number in ",c," attempts")

    
