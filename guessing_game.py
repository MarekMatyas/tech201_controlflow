correct_number = 5
user_guess = int(input("Please enter your guess."))
for number in range(3):
    if user_guess < 1 or user_guess > 20:
        print("Your guess is out of range!")
    elif user_guess > correct_number:
        print("Your guess is too high! ")
    elif user_guess > correct_number:
        print("Your guess is too high!")
    elif user_guess == 5:
        print("That's it! You guessed right.")
        break
else:
    print(f"The number I was looking for was {correct_number}.")
