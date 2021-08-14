#Write a program to determine that two lists have at least one common element.
nameList = ["Jean", "Jean", "Klee", "Alice", "Albedo"]

duplicate = nameList[0]

for i in range(0,len(nameList)):
    if nameList[i] == duplicate:
        duplicate == nameList[i]

nameList.remove(duplicate)

print(nameList)