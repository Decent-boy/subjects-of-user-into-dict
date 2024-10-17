# got subjects from user and marks and print these into dict:
dict={}
for i in range(3):
    user=input("enter the name of subject: ")
    marks=float(input("enter marks of subject: "))
    dict[user]=marks
print(dict)
