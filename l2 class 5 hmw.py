#given an input string count all lowercase, upper case, digits, and special symbols

def find_symbols(string, chars_l, chars_u, dig, spec):
    for i in string:
        if i.islower():
            chars_l += 1
        elif i.isupper():
            chars_u += 1
        elif i == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            dig += 1
        else:
            spec += 1

    output = "lower case =", chars_l, "upper case =", chars_u, "digits =", dig, "special =", spec,
    return output


stringA = str(input("Please type a string"))
chars_lower = 0
chars_upper = 0
digits = 0
specials = 0

print(find_symbols(stringA, chars_lower, chars_upper, digits, specials))

#Accept two int values from user and return their product. If the product is greater than 1000, then return their sum.
def multiplication(val1, val2):
    product = val1*val2
    return product

def addition (val1, val2):
    sum = val1+val2
    return sum

val1 = int(input("Please type a number"))
val2 = int(input("Please type another number"))

if multiplication(val1, val2) > 1000:
    print("The sum of value 1 and value 2 is", addition(val1, val2),)
else:
    print("The product of value 1 and value 2 is", multiplication(val1, val2),)

#Write a program to get a natural number n from the user, write a function to calculate the number n's harmonic number and return it to the caller.
def harmonic(natural_num):
    p = 0
    harm = 0
    for i in range(0, natural_num):
        p = p+1
        nt = 1/p
        harm = harm + nt

    return harm


natural_num = int(input("Please type a natural number"))

print(harmonic(natural_num))


#Write a function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num, fac):
    for i in range(1, num+1):
        fac = fac*i
    return fac

fac = 1

while True:
    num = int(input("Please enter a non-negative integer"))
    if num >= 0:
        break
    else:
        print("not supported")

print("The factorial of", num, "is", factorial(num, fac),)

#checkpoint


