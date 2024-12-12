def leapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): ##in all cases if it is divisible by 400 it is a leap year
        return True
    else:
        return False

year = int(input("Please type in a year : "))

if leapYear(year):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")