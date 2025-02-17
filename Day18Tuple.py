tuple1 = (1 , 2, 3 ,5 , 7)
print(type(tuple1))
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

tuple20 = tuple1 + tuple2
print(tuple20)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

tuple2 = (20 , 30 , 40)
print(tuple2)
if 40 in tuple2:
    print("Yes, 40 is in tuple2")
else:
    print("No, 40 is not in tuple2")

country = ("spain" , "America" ,  "Germany" , "NewYork ")
print(country[0])
print(type(country))
print(type(country[0]))
print(country[1])
print(country[2])
print(country[3])
print(country[0:3])
print(country[0:2])


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
songs = ("")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])
print(animals[5])
print(animals[6])
print(animals[7])
print(animals[8])

# Manupulating Tuple
tuple1 = (1 , 3 , 5 , 7 , 9 , 10 , 3 , 5 , 7 , 9)
res = tuple1.count(7)
print('Count of 7 in tuple1 is ' , res)
print('Index of 9 in tuple1  is' , tuple1.index(5))

print("Index of the first 7 in tuple1 is " , tuple1.index(7))   
