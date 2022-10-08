from Constants import constants as cons
from Repository import repository as repo
from TODO_item import todo_item
from datetime import datetime

class todo_service_item:
    def __init__(self):
        self.repo = repo.Repository()
        self.item = TODO_item.TODO_item
        self.status = cons.status

    def add_item(self, description: str, due_Date: str):
        due_date = datetime.strptime(due_Date, '%d-%m-%Y')
        self.item(description, due_date, self.status.pending, datetime.now())
        self.repo.create_item(self.item)

    def list_item(self):
        for task in enumerate(self.repo.find_all_item(), 1):
            print(*task)


# todo = todo_service_item()
# todo.add_item('hy', '10-11-1990')
# todo.add_item('hello', '05-12-2000')
# todo.list_item()






