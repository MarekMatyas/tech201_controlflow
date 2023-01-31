# Control flow

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

# In Python they are no 'switch statement' or 'case statements'.