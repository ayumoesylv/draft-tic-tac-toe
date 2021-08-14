numlist = [1, 2, 3, 4, 5]

minNumber = numlist[0]
MaxNumber = numlist[0]

for i in range(0, len(numlist)):
    if numlist[i] > MaxNumber:
        MaxNumber = numlist[i]
    if numlist[i] < minNumber:
        minNumber = numlist[i]

print(minNumber, MaxNumber)
