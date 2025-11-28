#For n situation:

# positional argument, keyword aargument
def test(*varagr,**para): # yah vararg/keyvararg bn gaya aur fir yah tuple bn jayega aur dictionary bn jayega respectively
    print(para)  


test(10,20,30,a=12,b=23,c=34,d=45,e=67,f=78)
test(12,23,345,a=12,b=23,c=34,d=45)
test(23,12,12,a=12,b=23)
test()