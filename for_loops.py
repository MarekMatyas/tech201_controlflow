# Looping

# A foor loop is where you define an iterator number and cycle through data (list or dictionary) `foreach` entry in that data structure.


# Creating a for loop

list_data = [1 ,2 ,3 ,4 ,5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)

# this will multiply EACH item on the `list_data` by 2

# nested for loops
# for data in embedded_lists:
#     print(data)
#     #This prints out both blocks, this gets inside the first square brackets
#     for num in data:
#         print(num)
#         #This prints out also individual items as well as the blocks. This get inside the individual brackets

# loops for dictionaries





# for item in dict_data.values():
#     print(item)
#     for embed_value in item.values():
#        print(embed_value)
#
# for items in dict_data.values():
#     print(item["money"])
# Please see Python documentation for more you can do with dictionaries and loops.

# Loops and if statements combined

list_1 = [1, 2, 3, 4, 5,]

for num in list_1:
    if num == 3:
        print("I found 3")
    elif num >3 :
        print("Gone too far!")
    else :
        print("Too soon")

## Too soon
# Too soon
# I found 3
# Gone too far!
# Gone too far!
## This is the output because it executes each item on the list from the beginning




