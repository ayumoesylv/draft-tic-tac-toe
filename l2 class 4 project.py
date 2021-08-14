string_list = ["abc", "xyz", "aba", "1221"]
integer_list = [1, 2, 3, 4]

#question 14
#count number of strings where length is 2 or more and 1st and last characters same

def count_a_list(list):
    restricted_count = 0
    for i in list:
        if len(i) >= 2 and i[0] == i[-1]:
            restricted_count = restricted_count + 1

    print(restricted_count)

count_a_list(string_list)

#question 15
#insert a given string at beginning of all items in integer list

def insert_in(nlist):
    for i in range(0, len(nlist)):
        nlist[i] = "emp"+str(nlist[i])

    print(nlist)

insert_in(integer_list)