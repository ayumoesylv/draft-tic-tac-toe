#Write a program that tkaes a string from the user and count the number of vowels and consonants
def question10():

    vowel_count = 0
    cons_count = 0

    vowel_list = ['a', 'e', 'i', 'o', 'u']

    user_string = str(input("Please type a word"))
    for i in user_string:
        if i in vowel_list:
            vowel_count = vowel_count + 1

        else:
            cons_count = cons_count + 1

    print(vowel_count, cons_count)

#Write a program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, print an error message.
def question11():
    while True:
        string_q11 = str(input("please type a string"))

        if (len(string_q11)) > 2:
            beginning = str(string_q11[0:2])
            end = str(string_q11[-2:(len(string_q11))])

            output_q11 = beginning + end
            print(output_q11)
            break

        else:
            print('must be greater than 2')

#Write a program to get a string from a given string where all occurrences of its first char have been changed to ʹ$ʹ, except the first char itself.
def question12():
    string_q12 = str(input("please type a string"))

    first_letter = string_q12[0]

    complement = string_q12[1:(len(string_q12))]

    for i in complement:
        if i == first_letter:
            complement = complement.replace(i, "$")

    print(first_letter+complement)

#Write a program to create a list containing a few names or a few words.
def question13():
    list1 = ["Apple", "  pencil  ", "Mushroom", "sauce"]
    five_letter = 0

    #print the original list
    print(list1)

    #remove leading and trailing whitespaces in all elements
    list1[1] = list1[1].strip()
    print(list1)

    #count the words with 5 letters
    for i in list1:
        if len(i) == 5:
            five_letter = five_letter + 1

    print(five_letter)

    #print all title words
    for i in list1:
        if i.istitle():
            print(i)

question10()
