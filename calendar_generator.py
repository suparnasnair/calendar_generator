# module imports
import argparse
import os

import html_generator

# dict to store the months
months = {1: 'January', 2: 'February', 3: 'March',
          4: 'April', 5: 'May', 6: 'June', 7: 'July',
          8: 'August', 9: 'September', 10: 'October',
          11: 'November', 12: 'December'}

# list containing number of days for a non leap year and
# leap year
non_leap_year = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]


def calculate_odd_days(year):
    """
    This function calculates the number of odd days for a given year
    :param year: the given year
    :return: the number of odd days
    """
    # to calculate odd days, use the logic that every 400 years will have 0 odd days
    odd_days = (year - 1) % 400
    # next, every 100 years have 5 odd days, so calculate this from the number of years remaining after
    # previous step
    # now, every leap year will have 2 odd days and every non leap year will have 1 odd day
    # calculate the number of leap years from the remaining years and multiply this by 2.
    # finally, sum all the numbers
    odd_days = (odd_days // 100) * 5 + ((odd_days % 100) - (odd_days % 100) // 4) + ((odd_days % 100) // 4) * 2
    # now, again consider the fact that every additional 7 days become a new week,
    # hence take the remaining number as odd days
    odd_days = odd_days % 7
    return odd_days


def is_leap_year(year):
    """
    This function checks whether a given year is a leap year or not
    :param year: the specified year
    :return: True if a leap year, else False
    """
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


def get_days_upto(year, month):
    """
    This function calculates the number of days upto a given month
    :param year: the specified year
    :param month: the specified month
    :return: number of days upto the given month in a year
    """
    days_upto = 0
    # get the number of days based on whether the given year
    # is a leap year or not
    if is_leap_year(year):
        for i in range(month - 1):
            days_upto += leap_year[i]
    else:
        for i in range(month - 1):
            days_upto += non_leap_year[i]
    return days_upto


def print_calendar(year, month, odd_days):
    """
    This function gives the calendar days of the given month and year.
    The odd days are considered here and are replaced with spaces '  '.
    :param year: the given year
    :param month: the given month
    :param odd_days: the number of odd days in the month of the year
    :return: a dict containing the days for the given month
    """
    month_calendar_data = []
    # variable used for white space filling
    # where date not present
    space = ''
    space = space.rjust(2, ' ')

    # uncomment the below two lines and the print statements to view the calendar
    # in console as well
    # print(months[month], year)
    # print('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')

    # choose the days based on the 30 day months, february and the 31 day months
    if month == 9 or month == 4 or month == 6 or month == 11:
        for i in range(30 + odd_days):
            if i < odd_days:
                month_calendar_data.append(space)
                print(space, end=' ')
                if (i + 1) % 7 == 0:
                    month_calendar_data.append("\n")
                    # print()
            else:
                month_calendar_data.append("{:02d}".format(i - odd_days + 1))
                # print("{:02d}".format(i - odd_days + 1), end=' ')
                if (i + 1) % 7 == 0:
                    # print()
                    month_calendar_data.append("\n")
    # case: Month is February, consider leap year
    elif month == 2:
        if is_leap_year(year):
            p = 29
        else:
            p = 28

        for i in range(p + odd_days):
            if i < odd_days:
                month_calendar_data.append(space)
                # print(space, end=' ')
                if (i + 1) % 7 == 0:
                    month_calendar_data.append("\n")
                    # print()
            else:
                month_calendar_data.append("{:02d}".format(i - odd_days + 1))
                # print("{:02d}".format(i - odd_days + 1), end=' ')
                if (i + 1) % 7 == 0:
                    # print()
                    month_calendar_data.append("\n")
    # case: 31 day months
    else:
        for i in range(31 + odd_days):
            if i < odd_days:
                month_calendar_data.append(space)
                # print(space, end=' ')
                if (i + 1) % 7 == 0:
                    # print()
                    month_calendar_data.append("\n")
            else:
                # print("{:02d}".format(i - odd_days + 1), end=' ')
                month_calendar_data.append("{:02d}".format(i - odd_days + 1))
                if (i + 1) % 7 == 0:
                    # print()
                    month_calendar_data.append("\n")
    # print('\n\n')
    return month_calendar_data


def get_calendar(year, month):
    """
    This function generates the complete calendar for the given month and year
    :param year: the specified year
    :param month: the specified month
    :return: the dict containing calendar data
    """
    # calculate odd days for the given year
    odd_days = calculate_odd_days(year)
    # calculate the number of days upto the given month
    days_upto = get_days_upto(year, month)
    # re-calculate odd days
    odd_days += days_upto % 7
    odd_days = odd_days % 7
    # print the calendar for the given year, month and odd days
    data = print_calendar(year, month, odd_days)
    return data


def get_year_calendar(year):
    """
    This function generates the complete calendar for the given year, for all months
    :param year: the specified year
    :return: a dict containing the days for each month
    """
    month_data = {}
    # iterate through each month and generate the calendar for the month
    for month in range(1, 13):
        month_data[months[month]] = get_calendar(year, month)
    return month_data


def generate_html_calendar(data, output):
    """
    This function is the wrapper for generating the html output
    :param data: the dict containing the calendar data
    :param year: the year for which calendar range needs to be generated
    :return: None
    """
    html_string = ''
    # generate html head, body and tail
    html_string += html_generator.generator_head()
    html_string += html_generator.generate_body(data)
    html_string += html_generator.generate_tail()
    # finally, write the result into an html file
    if not os.path.exists('Results'):
        os.makedirs('Results')
    with open(os.path.join('Results', f'{output}.html'), 'w') as obj:
        obj.write(html_string)


if __name__ == '__main__':
    """
    The main entry point for this application
    """
    # create an instance of argument parser class
    parser = argparse.ArgumentParser()
    # add the argument for year
    parser.add_argument('-y', '--year', help='add the calendar year',
                        type=int, required=True)
    parser.add_argument('-o', '--output', help='the file name of the generated html output', required=True)
    # parse args and get the year
    args = parser.parse_args()
    # now, generate calendar for the given year - 1, year and year + 1
    # and add it to a dict
    data = {args.year - 1: get_year_calendar(args.year - 1),
            args.year: get_year_calendar(args.year),
            args.year + 1: get_year_calendar(args.year + 1)}
    # finally, invoke the method to generate the calendar for the three years
    generate_html_calendar(data, args.output)
