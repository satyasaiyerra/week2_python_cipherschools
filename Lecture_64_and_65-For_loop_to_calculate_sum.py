total=0
num=input("Enter a number: ")
for i in range(0,len(num)):
    total += int(num[i])
print(total)


# Lecture 65
name = input("Enter a name: ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp+=name[i]