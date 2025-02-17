# default argument
def name (fname , mname = "singh" , lname = "dhiman"):
    print("hello" , fname , mname , lname)
name("Amitoj")

def average(c = 30 , d = 40):
    print("average of two numbers is " , (c+d)/2)
average(d = 50)
 
# #  keyword argument
def myname(fname, mname, lname):
    print("Hello,", fname, mname, lname)

myname(mname = "Peter", lname = "Wesker", fname = "Jade")

def keywords(b , c , a):
    print("hello" , a , b , c)
keywords(a = 50 , b = 60 , c = 70)
# required arguments should be check with
def numbers(a  , b = 50 , c = 40):
    print("additon of three numbers",a + b + c)
numbers (a = 50)

def average(*numbers):
  print(type(numbers))
sum = 0
for i in numbers:
   sum = sum + i
   print("Average is " , sum / len(numbers))

average(5 , 6 , 7 , 1)

def name( fname  , mname , lname ):
    print("hello" , fname , mname , lname );
name ("amitoj " , "singh " , "dhiman");
# Variable Length Arguments 
# Arbitary Arguments
# *name is also an iterable 
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")
