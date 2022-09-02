import datetime


def check_year(year):
    year_ = int(year)
    if year_ % 4 == 0 and year_ % 100 != 0:
        return True
    if year_ % 400 == 0:
        return True


def check_month(year, month):
    if month == '2' and check_year(year):
        return 29
    if month == '2':
        return 28
    if month == '4' or month == '6' or month == '9' or month == '11':
        return 30
    else:
        return 31


def check_num(date1, date2):
    d1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
    d2 = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
    num = (d2 - d1).days
    return num + 1


def get_between_day_list(days):
    date_list = []
    begin_date = datetime.datetime.strptime(f'{days[0][0]}-{days[0][1]}-{days[0][2]}', "%Y-%m-%d")
    end_date = datetime.datetime.strptime(f'{days[1][0]}-{days[1][1]}-{days[1][2]}', "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date = date_str.replace('-', ' ').split()
        date_list.append(date)
        begin_date += datetime.timedelta(days=1)
    return date_list
