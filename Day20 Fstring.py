# It is also known as literal string interpolatiion
country = "India"
name = "Amitoj Singh"
# purana method
# print(letter.format(country , name  , ))
# new method
print(f"Hey my name is {name} and I am from {country}")
price = 46.9037837
txt = f"For only {price:.2f} dollars"
print(txt)
print(txt.format())
print((f"{2 * 30}"))
print(type(f"{2 * 30}"))
print((f"{3 * 30}"))
print(f"We use the f-strings  like this : Hey my name is {{Amitoj Singh}} and I am from {{India }}")
print(f"We use the f-strings  like this : Hey my name is {name} and I am from {country}")
