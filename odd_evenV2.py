def number(user_choice: int) -> int:
    if user_choice:
        user_choice % 2 == 0
        return "Your number is even."
    else:
        return "You number is odd"



user_choice = int(input("Enter you number here:"))
print(number(user_choice))
