# 12. Monthly Calendar Display

import calendar

def display_calendar(year: int, month: int) -> None:
    '''
    This function will display the calendar for given month and year
    '''
    print('='*20)
    print(f'The calendar month for {year}/{month}')
    print('='*20)
    print(calendar.month(year, month))

if __name__ == '__main__':
    try:
        year = int(input('Enter the year(e.g. 2025): '))
        month = int(input('Enter the month(1-12): '))
        if 1 <= month <= 12:
            display_calendar(year = year, month = month)
        else:
            print('\nInvalid month. Please enter a number between 1 and 12 (inclusive)')
    except ValueError:
        print('\nError in value. Enter only numbers for year and month')