lst1 = [20 , 30 , 40 , "Amitoj Singh" , "Akash"]
lst2 = ["Red" , "Blue" , "Pink"]
lst3 = ["Name" , "Email" , "Conatact"]
print(lst1)
print(lst2)
print(lst1[0])
print(lst1[1])
print(lst1[2])
print(lst3)
print(type(lst1))
print(type(lst2))
print(type(lst3))

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])


colors = ["Red", "Green", "Blue", "Yellow", "Green"]

print(colors[0])
print(colors[-3])
print(colors[-5])


if "Yellow" in colors:
     print("Yes")
else:
     print("No")

l1 = [57 , 50 , 30 , 20 , 60]
l1.sort()
l1.reverse()
l1.append(8)
l1.append(9)
l1.append(7)
l1.remove(50)
l1.remove(30)
l1.remove(60)
print(l1)
 
marks = [20 , 30 , 40 , 50 , 60]  
#       -5    -4   -3   -2    -1 (negative indexing)
#       0     1    2    3     4 (positive indexing)
print(marks[-3])
print(marks[-4])
print(marks[-5])
print(marks[-2])

if "30" in marks:
     print("Yes")
else:
     print("No") 
print(marks[1 : -1])
print(marks[1 : 3])
print(marks[1 : 4])
print(marks[1 : 5])
print(marks[1 : 4 :2])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
#          0       1       2       3       4       5       6        7       8         [Postive Index]
#          -9      -8      -7      -6      -5      -4      -3       -2      -1       [Negative Index]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

StudentMarks = [20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
#              0    1    2    3    4    5    6    7    8
#              -9   -8   -7   -6   -5   -4   -3   -2   -1
Students = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
print(Students[4:5])
print(StudentMarks[2:5])
print(StudentMarks[-6:-5])

# List Comprehensions
names = ["Amitoj Singh" , "Krishna" , "Jagjeet Singh" , "Rahul Bhatt" , "Akash" ]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
nameWith = [item for item in names if "A" in item]
nameWith = [item for item in names if "j" in item]
nameWith = [item for item in names if "S" in item]
nameWith = [item for item in names if "h" in item]
print(nameWith)

# lst = [i*i for i in range(10)]
# print(lst)
lst = [i * i for i in range(10) 
     if i % 2 == 0
     if i % 3 == 0
     if i % 5 == 0
]
print(lst)