#Write a function to check whether a passed string is a palindrome or not.
def palindrome(string):
    string_rev = string[::-1]
    if string == string_rev:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome")

q34string = str(input("Please type a word"))
palindrome(q34string)

#Write a function to check whether a string is a pangram or not
def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in string.lower():
            return ("This is not a pangram")

    return("This is a pangram")


q35string = str(input("Please input a string"))
print(pangram(q35string))

#Write a program to create a Caesar encryption. Create 2 functions encode and decode
#Encode accepts a plain text string and output an encrypted string
#Decode accepts an encrypted text string and output an plaintext string
def encode(string, shift):
    encryption = ""
    for i in string:
        if i.isupper():
            new_shift = ord(i) + shift
            new_index = new_shift - ord("A")
            p = chr(new_index % 26 + ord("A"))
            encryption = encryption + p

        elif i.islower():
            new_shift = ord(i) + shift
            new_index = new_shift - ord("a")
            p = chr(new_index % 26 + ord("a"))
            encryption = encryption + p

    return encryption



def decode(string, shift):
    decryption = ""
    for i in string:
        if i.isupper():
            new_shift = ord(i) - shift
            new_index = new_shift - ord("A")
            p = chr(new_index % 26 + ord("A"))
            decryption = decryption + p

        elif i.islower():
            new_shift = ord(i) - shift
            new_index = new_shift - ord("a")
            p = chr(new_index % 26 + ord("a"))
            decryption = decryption + p

    return decryption

q36string = str(input("Please type a sentence"))
shift = 5

q36string2 = encode(q36string, shift)
print(encode(q36string, shift))
print(decode(q36string2, shift))

#checkpoint