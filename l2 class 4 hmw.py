def question16():
    string = str(input("type a sentence with not and poor"))

    list_input = string.split()

    has_not = 0
    has_poor = 0

    for i in range(0, len(list_input)):
        if list_input[i] == "not":
            print("there is a not")
            has_not = has_not + i

        elif list_input[i] == "poor":
            print("there is a poor")
            has_poor = has_poor + i

    if has_not < has_poor:
        list_input[has_not:has_poor + 1] = "good"

    print(list_input)

question16()

#question 17
og_str = str(input("Please enter a string"))
def question17(og):
    return og[::-1]

print(question17(og_str))

#question 18
hyphen_str = str(input("type a sentence using hyphens as separators of words."))
def question18(string_h):
    string_h = string_h.split('-')
    string_h.sort()

    hyphen = "-"
    hyphen = hyphen.join(string_h)

    return hyphen

print(question18(hyphen_str))

#question 19
listA = str(input("Please type a few sentences using the word emma at least once"))
def question19(input):
    input = input.split(" " or ".")
    count_word = 0

    for i in input:
        if i == "emma":
            count_word += 1

    print("emma appears", count_word, "times in the string.")


question19(listA)