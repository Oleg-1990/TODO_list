from datetime import datetime


def validate_date(date: str):
        try:
            mod_date = datetime.strptime(date, '%d.%m.%Y')
        except:
            return False
        else:
            return mod_date

def valid_index(len_list: int):
    flag = False
    while not flag:
        index = input().strip()
        if index.isnumeric() and 1 <= int(index) <= len_list:
            flag = True
            return int(index)
        else:
            print('You entered an invalid index, please try again')




