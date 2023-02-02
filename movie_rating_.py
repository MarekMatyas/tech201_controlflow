def film_rating_description(rating):
    rating = rating.lower()
    if rating == "universal":
        return "This age group can watch this film."
    elif rating == "pg":
        return "General viewing but parental guidance advised."
    elif rating == "12" or rating == "12a":
        return "12 rated movies may not be suitable for those under 12, but supervision is recommended."
    elif rating == "15":
        return "you must be 15 years or older to watch this."
    elif rating == "18":
        return "You must be 18 years or older to watch this."
    else:
        return "This is not a correct rating, please use universal, pg, 12, 15, 18."

film_rating = "universal"
print(film_rating_description(film_rating))
