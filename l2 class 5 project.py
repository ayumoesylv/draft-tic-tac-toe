#Given a string of odd length greater 7, return a string made of the middle 3 chars of a given string
def getMiddleThreeChars(word):

    p = int((len(word) - 3)/2)
    word = word[p:(len(word)) - p]

    return word

while True:
    sample = str(input("Please enter an odd numbered length string"))
    if len(sample)%2 == 0:
        print("not supported")
    else:
        break

print(getMiddleThreeChars(sample))