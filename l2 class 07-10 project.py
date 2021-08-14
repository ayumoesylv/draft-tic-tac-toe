#write a program to replace the last element in a list with another list.

listA = [1, 3, 5, 7, 9, 10]
listB = [2, 4, 6, 8]

listA[(len(listA) - 1)] = listB

print(listA)

#teacher's method
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

del(list1[-1])
list1.extend(list2)
print(list1)