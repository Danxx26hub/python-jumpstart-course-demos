import datetime

def print_header():
    print('_' * 50)
    print('            BIRTHDAY APP!   ')
    print('_' * 50)
    print()


def get_birthday_from_user():
    print('when were you born?')
    year = int(input('Year  [yyyy]'))
    month = int(input('month [mm]'))
    day = int(input('day [dd]'))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)


    dt = this_year - target_date
    return dt.days



def print_birthday_information(days):
    if days < 0:
        print('you had your birthday {} days ago this year'.format(-days))
    elif days > 0:
        print('your birthday is in {} days'.format(days))
    else:
        print('happy bday!!!!')
    


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()
