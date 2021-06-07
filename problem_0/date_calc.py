







print("Welcome!\nThis is a date calculator and this is the way it works")
print("You will be asked to add an initial date in the format DD/MM/YYYY\nThen you will be asked to add an end date in the same format as the initial one. Afterwards, the calculator will provide you with the amount of days that have elapsed between your two dates. Please note, the difference between a date and day inmmediately afterwards is 0, meaning this calculator is not inclusive of its end points.")

def is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def date_calc(start, end):
    
    days_in_months      = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day1, month1, year1 = map(int, start.split('/'))
    day2, month2, year2 = map(int, end.split('/'))
    
    day1 += 1
#     day2 -= 1
    

    year_to_days = int((year2 - year1) * 365)

    if is_leap(year1):

        if month1 != 1:
            months_to_days1 = sum(days_in_leap_months[:month1 - 1]) + day1
        else:
            months_to_days1 = day1
    else:
        if month1 != 1:
            months_to_days1 = sum(days_in_months[:month1 - 1]) + day1
        else:
            months_to_days1 = day1



    if is_leap(year2):
#             year_to_days += 1
        if month2 != 1:
            months_to_days2 = sum(days_in_leap_months[:month2 - 1]) + day2
        else:
            months_to_days2 = day2
    else:
        if month2 != 1:
            months_to_days2 = sum(days_in_months[:month2 - 1]) + day2
        else:
            months_to_days2 = day2
            
    leap_years_between = []
    sorted_years = sorted((year1, year2))
    
    for y in range(sorted_years[0], sorted_years[1] + 1, 1):
        if is_leap(y):
            leap_years_between.append(1)
    
    leap_years_between = sum(leap_years_between)
    
    if leap_years_between == 2:
        leap_years_between -= 2
    elif leap_years_between == 1:
        leap_years_between -=1
    
    months_in_between = months_to_days2 - months_to_days1
        
        
    your_num = abs(year_to_days + months_in_between + leap_years_between)
    
    print(f"There are {your_num} days in between your dates")

activate = True

while activate == True:
    
    date1 = input("Please enter a starting date (DD/MM/YYYY): ")
    date2 = input("Please enter an ending date (DD/MM/YYYY): ")
    
    date_calc(date1, date2)
    
    continuation = input("Would you like to calculate another date (yes/no): ").lower()
    
    if continuation == 'no':
        print("Thanks for using our services. Please come back again soon.")
        activate = False
    else:
        print("Let's try another one.")
        
    