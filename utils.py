from datetime import datetime
from Constants import constants as con
from termcolor import colored


def color_of_status(status: str):
    if con.status.completed in status:
        return colored(con.status.completed, 'green')
    elif con.status.canceled in status:
        return colored(con.status.canceled, 'red')
    else:
        return colored(con.status.pending, 'yellow')


def computer_date(date: str):
    if date is None:
        return None
    else:
        return datetime.strptime(date, '%d-%m-%Y')


def beautifull_date(date):
    if date is None:
        return None
    else:
        return date.strftime('%d-%m-%Y')

