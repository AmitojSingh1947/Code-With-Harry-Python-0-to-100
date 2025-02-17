appleprice = 200
apple = 210
if(apple <= appleprice):
    print("yes")
else:
    print("no")

# elif Statements
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

num = int(input("enter your age "))
print("your age is " , num )
if (num >100):
    print("your age is smaller than 100")
else:
     print("your age is greater than 100")

print("yeh bro")

n1 = input("enter the name of person")
print("name of person" ,n1 )
if (n1 == "amit"):
    print("your name is matched")
elif(n1 != "amitoj"):
    print("your name is half matched")
else:
    print("your name is not matched")
print("your name is dicard")

# Nested if statements
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")