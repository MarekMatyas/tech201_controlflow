# tech201_controlflow
# Control flow

## if, elif, else

`if` `elif` `else` statements is a control flow structure in Python programming that allows a program to evaluate multiple expressions and execute code block based on the conditions being met.
`else` catches everything else if the criteria weren't met.
`else` statement will be executed if all the conditions under the `if` and `elif` statements are `False`.

## `if` statement

The `if` statement is **conditional statement in Python, that is used to determine whether a block of code will be executed or not**. Meaning if the program find the condition defined in the `if` statement to be true, it will go ahead and execute the code block inside the `if` statement.

## `elif` statement

`elif` statement is short for **"else if"** and is used when the first `if` statement isn't true, but you want to check for another condition.

## `else` statement 

The `else` statement **specifies that alternate processing is to take place when the conditions of previous `if` statements are not satisfied**. The `else` statement has no parameters and it must be column-aligned with the matching `if` statement. 

### ***Quick example***

```
film_rating = "16"
if film_rating.lower() == "universal":
     print("All age groups can watch this film.")
elif film_rating.lower()== "pg":
    print("General viewing but parental guidance advised.")
elif film_rating.lower()== "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12, but supervision is recommended.")
elif film_rating.lower()== "15":
    print("you must be 15 to watch this.")
elif film_rating.lower()== "18":
    print("You must be 18 to watch this ")
else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18.")
```
In Python they are no 'switch statement' or 'case statements'.

## `for` loops

A `for` loop is where you define an iterator numer and cycle through data (list, dictionary) `foreach` entry in that data structure.

Let's create a simple example:

First create a list or dictionary.

``` 
list_data = [1 ,2 ,3 ,4 ,5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}
```