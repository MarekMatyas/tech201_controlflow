hours_worked = int(input("Please enter your hours for this week."))
hourly_rate = int(input("Thank you, now enter your hourly rate."))



if hours_worked > 40:
    overtime = hours_worked - 40
    gross_pay = (40 * hourly_rate) + (overtime * hourly_rate * 1.5)
else:
    gross_pay = hours_worked * hourly_rate
print(f"Your income for this week is £{gross_pay}, have fun !!")

