for fizz_buzz_number in range(1, 101):
     if fizz_buzz_number % 3 == 0 and fizz_buzz_number % 5 == 0:
          print("FizzBuzz")
     elif fizz_buzz_number % 3 == 0:
          print("Fizz")
     elif fizz_buzz_number % 5 == 0:
         print("Buzz")
     else:
         print(fizz_buzz_number)
