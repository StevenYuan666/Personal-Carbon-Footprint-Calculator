# COMP 202 A1: Part 1
# Unit Conversion
# Author: Ye Yuan
#Student ID:260921269

import doctest
INCOMPLETE = -1

# You may find these constants important... :)
POUND_IN_KG = 0.45359237
KM_IN_MILES = 0.621371
DAYS_IN_YEAR = 365.2425


def kg_to_tonnes(kg):
    '''(num) -> float
    Convert mass in kg to in metric tonnes. 1000 kg = 1 tonne.
    >>> kg_to_tonnes(0)
    0.0
    >>> round(kg_to_tonnes(723), 4)
    0.723
    >>> round(kg_to_tonnes(0.5), 4)
    0.0005
    '''
    tonnes=kg/1000#divide the input value of parameter kg by 1000 and set the result to the new variable tonnes
    return tonnes#then return the value of tonnes


def pound_to_kg(lbs):
    '''(num) -> float
    Convert lbs to kg. 1 lbs is 0.453592 kg.
    >>> pound_to_kg(0)
    0.0
    >>> round(pound_to_kg(1), 4)
    0.4536
    >>> round(pound_to_kg(23), 4)
    10.4326
    '''
    kilograms=lbs*POUND_IN_KG#multiply the input value of paramter lbs with the constant POUND_IN_KG, and set the result to the new variable kilograms
    return kilograms#then return the value of kilograms


def km_to_miles(km):
    '''(num) -> float
    Convert km to miles.
    >>> km_to_miles(0)
    0.0
    >>> round(km_to_miles(100), 4)
    62.1371
    >>> round(km_to_miles(5), 4)
    3.1069
    '''
    miles=km*KM_IN_MILES#multiply the input value of parameter km with the constant KM_IN_MILES, and set the result to the new variable miles
    return miles#then return the value of miles


def daily_to_annual(daily_value):
    '''(num) -> float
    Convert a daily_value to an annual value, 
    using number of days in Gregorian year (365.2425 days).
    >>> daily_to_annual(0)
    0.0
    >>> round(daily_to_annual(1), 4)
    365.2425
    >>> round(daily_to_annual(1000), 4)
    365242.5
    '''
    days_from_daily_value=daily_value*DAYS_IN_YEAR#multiply the input value of parameter daily_value with the constant DAYS_IN_YEAR, and set the result to the new variable days_from_daily_value
    return days_from_daily_value#then return the value of days_from_daily_value


def weekly_to_annual(w):
    '''(num) -> num
    Convert a weekly amount into an annual
    amount assuming a Gregorian year of 365.2425 days.

    >>> weekly_to_annual(0)
    0.0
    >>> round(weekly_to_annual(1), 4)
    52.1775
    >>> round(weekly_to_annual(1.25), 4)
    65.2219
    '''
    days_from_weekly_value=(w/7)*DAYS_IN_YEAR#divide the input value of parameter w with 7, since to there are 7days in a week, and then multiply it with the constant DAYS_IN_YEAR, then set the result to new variable days_from_weekly_value
    return days_from_weekly_value#return the value of days_from_weekly_value


def annual_to_daily(annual_value):
    '''(num) -> float
    Convert a annual_value to a daily value, using number of days in Gregorian year.
    >>> annual_to_daily(0)
    0.0
    >>> annual_to_daily(365.2425)
    1.0
    >>> round(annual_to_daily(356), 4)
    0.9747
    '''
    years_from_annual_value=annual_value/DAYS_IN_YEAR#divide the input value of parameter annual_value by the constant DAYS_IN_YEAR, and set the value to the new variable years_from_annual_value
    return years_from_annual_value#then return the value of years_from_annual_value


if __name__ == '__main__':
    doctest.testmod()
