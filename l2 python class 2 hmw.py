import random


#given an integer or floating number list, do the following
def question7():
    """deals with elements in a list"""

    #Print out the elements which are less than 5 one by one
    numList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for i in numList:
        if i < 5:
            print(i)

    #Make a new list that contains all the elements less than 5 and print out the new list

    result = [i for i in numList if i < 5]
    print(result)

    #Ask the user for a number and create a list which only contains the elements smaller than that number.
    while True:
        guest_bound = 0
        try:
            guest_bound = int(input("please enter a number"))
            break
        except:
            print("input invalid")

    result2 = [i for i in numList if i < guest_bound]
    print(result2)


#write a program to create a list containing 100 random integers between 0 and 1000.
def question8():
    """does something"""

    rand_list = [random.randint(0, 1000) for i in range(100)]

    #Calculate the average for all elements
    sum_of_list = sum(rand_list)
    average = sum_of_list/100

    print(average)

    #Count how many odd numbers are in the list
    odd_num = 0
    for i in range(0, len(rand_list)):
        if i % 2 != 0:
            odd_num = odd_num + 1

    print(odd_num)

    #Sum up all the even numbers in the list
    even_list = [i for i in rand_list if i % 2 == 0]
    print(even_list)
    sig_even = sum(even_list)

    print(sig_even)

    #Find out the maximum and minimum elements
    max_elm = rand_list[0]
    min_elm = rand_list[0]

    for i in range(0, len(rand_list)):
        if rand_list[i] > max_elm:
            max_elm = rand_list[i]
        if rand_list[i] < min_elm:
            min_elm = rand_list[i]

    print(min_elm, max_elm)


#Write a program to convert a list of integers into a single integer
def question9():
    """converts a list of integers into a single integer"""

    final_integer = str("")

    list_a = [11, 33, 50]

    for i in range (0, (len(list_a) - 1)):
        final_integer = str(list_a[i]) + str(list_a[i+1])

    print(final_integer)


question7()