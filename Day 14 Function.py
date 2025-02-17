def calculateGmean(a , b):
    mean = (a*b)/(a+b)
    print(mean)

a = 40
b = 30
calculateGmean(a , b)
if(a > b):
    print("first number is greater")
else:
    print("second number is greater")

def calculateGmean(c , d):
    mean = (c*d)/(c+d)
    print(mean)

c = 40 
d = 50
if(c > d):
     print("first number is greater c is greater")
else:
    print("second number is greater means d is greater")

calculateGmean(c , d)

def isgreater(a , d):
    mean = (a*d)/(a+d)
    print(mean)
    if(a < d):
        print("First is greater ")
    else:
        print("second is greater")
    
    a = 40
    d = 50
    isgreater(a , d)
 
# # calling a function
def myname(fname  , lname):
    print("hello" , fname , lname)
myname("amitoj" , "singh")
# def calculategmean(a , b):
#     mean = (a*b)/(a+b)
#     print(mean)
 
# def isgreater(a ,b):
#     if(a > b):
#         print("first number is greater"); 
#     else:
#         print("Second number is greater");
# a = 20 
# b = 30
# calculategmean(a , b)
# isgreater(a , b)

# # calling a function 
# def name (fname , lname):
#     print("hello" , fname , lname);
# name("Ajay" , "Singla")