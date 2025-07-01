# 14. Days Between Dates

from datetime import date

def calculate_days(start_date: date, end_date: date) -> int:
    '''
    Calculates the number of days between given two date objects.

    Args:
        start_date (date): The earliest date
        end_date (date): The latetr date

    Returns:
        int: number of days between two dates
    '''
    return (end_date - start_date).days

if __name__ == '__main__':
    start_date = date(2014, 7, 2)
    end_date = date(2014, 7, 11)
    diffdays = calculate_days(start_date, end_date)
    print(f'Starting date: {start_date}')
    print(f'Ending date: {end_date}')
    print(f'Difference between two dates: {diffdays} days')
