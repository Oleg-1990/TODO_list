from datetime import datetime


def validate_date():
    flag = False
    mod_date = None
    print('Please enter due date in format dd.mm.yyyy')
    while not flag:
        try:
            date = input().strip()
            mod_date = datetime.strptime(date, '%d.%m.%Y')
        except:
            print('You entered an invalid date, please try again in format dd.mm.yyyy.')
        else:
            flag = True
    return mod_date


def beautifull_date(date):
    if date is None:
        return None
    else:
        return date.strftime('%d-%m-%Y')

def computer_date(date: str):
    if date is None:
        return None
    else:
        return datetime.strptime(date, '%d-%m-%Y')


def valid_index(len_list: int):
    flag = False
    while not flag:
        index = input().strip()
        if index.isnumeric() and 1 <= int(index) <= len_list:
            flag = True
            return int(index)
        else:
            print('You entered an invalid index, please try again')
