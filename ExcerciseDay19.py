import time 
timestamp = time.strftime('%H : %M : %S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the Hour:"))
print(hour)

if(hour>=0 and hour < 12):
    print("Good Morning")
elif(hour>=12 and hour < 18):
    print("Good Afternoon")

# 1 Exercise Cororpati Pati Game
# 2  Use List Data Type to Store the questiions and their correct answer
# List of tuples: each tuple contains a question and the correct answer
qa_list = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is 2 + 2?", "4"),
    ("What is the largest planet in our solar system?", "Jupiter")
]

# Example: Accessing a question and its answer
# formatted strings
for question, answer in qa_list:
    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print()

for question, answer in qa_list:
    print(f"Question: {question}")
    print(f"Answer: {answer}")

# letter = "Hey My name is {} and I am from {}"
# name = "amitoj"
# country =  "India"
# print(letter.format(name , country))

# I use f string 
lst = [
    ("Mera naam ke ha ", "Amitoj Singh"),
    ("Mah Kitho da Rehan Vala Ha" , "Patiala")
]
for question , answer in lst:
    print(f"Question: {question}")
    print(f"Answer: {answer}")
