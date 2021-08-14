#Write a function that takes a list and returns a new list with unique elements of the first list.
def unique_count(list):
    new_list = []

    for i in list:
        if i not in new_list:
            new_list.append(i)

    return new_list
first_list = [1,2,3,3,3,3,4,5]
print(unique_count(first_list))

