# While loops

# not as common as for loops

# While loops monitor data rather than iterate

x =0

#  conditions are met
#  while x < 10:
# #     print(f"It's working -> {x}")
# #     x += 1  # increment
# # # This will add 1 extra  to the x with each loop until the conditions are met

# using break

# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1
# # using the break it stops the loop at a defined condition
# print(x)

#use while to verify user input
# This can be either an int (20) or string (twenty)

# age = input("What is your age ? ")
#
# print(f"your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117:     #checks if the user input is in correct format and sets a limit of the input
        user_prompt = False
    else:
        print("Please provide your answer in digits and below 117.")       # if the user input is in wrong format else statement will print out this message

print(f"Your age is {age}")


