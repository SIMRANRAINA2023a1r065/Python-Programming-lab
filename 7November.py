#Multilevel Inheritance
class Parent1:
    def fun1(self):
        print("Hello from fun1")
class Parent2(Parent1):
    def fun2(self):
        print("Hello from fun2")
class child(Parent2,Parent1): #child pehle aata hai fir parent aata hai nhi toh MRO(Method Resolution Order) error aayega, when u are inheriting 2 parents saath m and dono m parent-child relationship hai
    def fun3(self):
        print("Hello from fun3")

ob=child()
ob.fun1()
ob.fun2()
ob.fun3()
# Abstract classes: jisme functionality nhi hoti...bs definition hoti hai , have/ have not incomplete methods, can`t make an object of abstract class`
# e.g; A fly is a abstract class of a bird that can`t be defined only mentioned there.

#Code: eg; method overriding
from abc import ABC,abstractclassmethod   # for  making a class abstract fn
class MediaPlayer(ABC): #ABC is abstrct base class
    def playAudio(self): #can give definition of it
        print("Can play audio!")
    @abstractclassmethod
    def playvedio(self):
        pass

# ob=MediaPlayer()
# ob.playvedio()
 #overwrite sirf child kr skta hai
class SoundRecorder(MediaPlayer):
    def playvedio(self):
        print("I can`t play vedio !")
class VlCPlayer(MediaPlayer):
    def playvedio(self):
        print("I can`t play vedio !")

sr=SoundRecorder()
sr.playAudio()
sr.playvedio()

vlc=VlCPlayer()
vlc.playAudio()
vlc.playvedio()

#2
from  abc import ABC,abstractclassmethod
class Bird(ABC):
    def speak(self):
      print("i can`t speak !")

@abstractclassmethod
def fly(self):
    pass

class Parrot(Bird):
    def fly(self):
        print(" i can`t fly !")
# class Penguin(Bird):
#     def speak(self):
#         print(" i can`t speak !")

ob=Parrot()
ob.fly()
# ob=Penguin()
ob.speak()

#ob:Bird=Parrot() # Parent:Child hinting possible hai

#Practice eg;

# class: shape name , 2 rules: print perimeter, print araea, 3 sub classes: circle,triangle, square
from abc import ABC,abstractclassmethod
class Shape(ABC):
     @abstractclassmethod
     def printarea(self):
        pass
     @abstractclassmethod
     def printperimeter(self):
        pass

class Circle (Shape):
    def printarea(self):
        print("area of circle:",3.14*4*4)
    def printperimeter(self):
        print("perimeter of circle:", 2*2.14*8)
class Triangle (Shape):
    def printarea(self):
        print("area of triangle:", 1/2* 4*9)
    def printperimeter(self):
        print("perimeter of triangle:", 2*2.14*8)
class Square (Shape):
    def printarea(self):
        print("area of square:", 4*7)
    def printperimeter(self):
        print("perimeter of square:", 7*9*9)

ob=Circle()
ob.printarea()
ob.printperimeter()
ob=Triangle()
ob.printarea()
ob.printperimeter()
ob=Square()
ob.printarea()
ob.printperimeter()


