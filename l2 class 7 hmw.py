# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5.
def question43(lst):
    new_list = []
    for n in lst:
        if n % 5 == 0:
            new_list.append(n)

    return new_list


def unique_count(lst):
    uniques = []

    for n in lst:
        if n not in uniques:
            uniques.append(n)

    return uniques


# Write a function to print the even numbers from a given list
def even_elements(lst):
    even_numbers = []
    for n in lst:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers


# driver code
input_numbers = input("Please type numbers separated by spaces")
# [5, 2, 4, 5, 7, 7, 7, 10, 0, 0, 3, 9, 6]
num_list = input_numbers.split()

for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])

# question 43
list_multiples = question43(num_list)
print("The multiples of 5 in", num_list, "are:")
for i in list_multiples:
    print(i)

# question 44
unique_list = unique_count(num_list)
print("The unique numbers in", num_list, "are", unique_list)

# question 46
even_list = even_elements(num_list)
print("The even numbers from", num_list, "are", even_list)

# checkpoint
