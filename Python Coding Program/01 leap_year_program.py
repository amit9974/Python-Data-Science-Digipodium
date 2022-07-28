# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, 
# otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
# It is only necessary to complete the is_leap function.
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


while True:
    def leap_year(year):
        year = int(input("Enter the year for check is leap or not : "))
        leap = False
        if year%4 ==0:
            leap = True
            print(f"{year} is leap year")
        elif year%400 == 0:
            leap = True
            print(f"{year} is leap year")
        elif year%100 == 0:
            leap = False
            print(f"{year} is not leap year")
        return leap

    leap_year(1900)