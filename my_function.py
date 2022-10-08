import Constants.constants as cons
from datetime import datetime
from colorama import Fore

def validate_date():
    flag = False
    mod_date = None
    print('Please enter due date in format dd.mm.yyyy')
    while not flag:
        try:
            date = input().strip()
            mod_date = datetime.strptime(date, '%d.%m.%Y')
        except:
            print('You entered an invalid date, please try again in in format dd.mm.yyyy.')
        else:
            flag = True
    return mod_date

def beautifull_date(date: datetime):
    return date.strftime('%d-%m-%Y')



# def priority(priority: str):
#     match priority:
#         case 'y':
#             return Fore.RED+cons.status.pending
#         case 'yes':
#             return Fore.RED + cons.status.pending
#         case 'n':
#             return cons.status.pending
#         case 'no':
#             return cons.status.pending
#         case 'not':
#             return cons.status.pending


