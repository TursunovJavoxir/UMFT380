def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        a = "высокосный"
    else: 
        a = "Невысокосный"
    return a