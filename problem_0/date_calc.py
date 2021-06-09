# Date Calculator CLI App

## Greet users
print()
print()

print("Welcome to the date calculator app!")

print()
print()

print("""You will be asked to add a starting date in the format DD/MM/YYYY,
then you will be asked to add an end date in the same format as the
initial one. Afterwards, the calculator will provide you with the
amount of days that have elapsed between your two dates. Please note,
the difference between a start and end date without any days in between
(e.g. 21/12/2000 and 22/12/2000) is 0, meaning this calculator will not
include the end points of your dates.""")

print()
print()

def is_leap(year):
    """
    This function will take a year and return a boolean if it a leap year
    year -> 1 if leap year, else 0.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



def date_calc(start, end):
    """
    start: string containing DD/MM/YYYY
    end: string containing DD/MM/YYYY
    """
    
    # these arrays will be used to calculate the days within the months provided
    days_in_months      = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    # Check if the dates have been separated by a /
    if len(start.split('/')) != 3 or len(end.split('/')) != 3:
        return None
    else:
        day1, month1, year1 = map(int, start.split('/'))
        day2, month2, year2 = map(int, end.split('/'))
    
    # We add a day to discard the initial point
    day1 += 1
    
    # convert the year to year difference into days
    year_to_days = int((year2 - year1) * 365)


    if is_leap(year1):
        # we don't count January as it is the start of the year and we would only need to add the days
        if month1 != 1:
            # otherwise we sum up the respective list of days within each month in a leap year
            # since python counts from 0 onwards, we subtract a day to avoid summing up the days
            # in the month chosen
            months_to_days1 = sum(days_in_leap_months[:month1 - 1]) + day1
        else:
            months_to_days1 = day1
    else:
        # same operation if the year is not a leap one but using the other array
        if month1 != 1:
            months_to_days1 = sum(days_in_months[:month1 - 1]) + day1
        else:
            months_to_days1 = day1


    # same operation as above but for year2
    if is_leap(year2):
        if month2 != 1:
            months_to_days2 = sum(days_in_leap_months[:month2 - 1]) + day2
        else:
            months_to_days2 = day2
    else:
        if month2 != 1:
            months_to_days2 = sum(days_in_months[:month2 - 1]) + day2
        else:
            months_to_days2 = day2
            
    
    # sort the years, and create an empty list that will contain a 1 for every leap
    # year between the years choosen. Then loop over the range of years (add 1 because
    # python doesn't count the ending point) and count the leap ones
    sorted_years = sorted((year1, year2))
    leap_years_between = []
    
    for y in range(sorted_years[0], sorted_years[1] + 1, 1):
        if is_leap(y):
            leap_years_between.append(1)
    
    # sum up the results
    leap_years_between = sum(leap_years_between)
    
    # account for those extra days in the months
    if leap_years_between >= 2: leap_years_between -= 2
    elif leap_years_between == 1: leap_years_between -=1
    
    # get the days between the months chosen
    months_in_between = months_to_days2 - months_to_days1
        
    # final calculation
    your_num = abs(year_to_days + months_in_between + leap_years_between)
    
    
    return your_num

    
# This will keep our while loop running untill we tell it to stop
activate = True

while activate:
    
    # prompts for the user to input the dates of interest
    date1 = input("Please enter a starting date (DD/MM/YYYY): ")
    date2 = input("Please enter an ending date (DD/MM/YYYY): ")
    print()
    
    date_answer = date_calc(date1, date2)
    
    # apply our function
    if date_answer:
        print(f"There are {date_answer} days in between your dates")
    else:
        print("Please try again using the date format DD/MM/YYYY")
        continue
        
    print()
    
    # ask the user if they would like to continue or not
    continuation = input("Would you like to calculate another date (yes/no): ").lower()
    print()
    
    # change activate to False if no
    if continuation == 'no':
        print("Thanks for using our services. Please come back again soon.")
        activate = False
    else:
        # keep going if yes
        print("Let's try another one.")
        
    
