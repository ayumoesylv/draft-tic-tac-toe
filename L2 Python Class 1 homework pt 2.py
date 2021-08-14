#write a program to count the number of elements in a list.

FruitIndex = ["apple", "orange", "banana", "kiwi", "blueberry", "grape"]
fruitNum = len(FruitIndex)

for i in range(0, len(FruitIndex)):
    print(FruitIndex[i], end = " ")

print("total:", fruitNum)