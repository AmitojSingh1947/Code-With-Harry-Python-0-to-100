# Sort Method Used
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# Reserve Method Used
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# index()
colors = ["voilet", "indigo", "blue", "green" , "red" , "Orange " , "green" , "blue" , "blue" , "Orange"]
        #  0    ,     1     ,   2    ,    3    ,   4   ,   5    positive indexing
newlist = colors.copy()
# print(colors.index("blue"))
# print(colors.index("red"))
# print(colors.index("green"))
print(colors.count("green"))
print(colors.count("blue"))
print(colors.count("Orange"))
print(newlist)
# append Method Used
colors.append("pink")
colors.append("yellow")
colors.append("black")
colors.append("white")
colors.append("purple")
colors.append("darkBlue")
colors.append("LightBlue")
colors.append("DarkGreen")
print(colors)