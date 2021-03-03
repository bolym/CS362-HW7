
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return "Not a leap year!"
        return "Leap Year!"