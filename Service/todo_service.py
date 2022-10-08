from Constants import constants as cons
from Repository import repository as repo
from TODO_item import todo_item
from datetime import datetime

class todo_service_item:
    def __init__(self):
        self.repo = repo.Repository()
        self.item = todo_item.TODO_item
        self.status = cons.status

    def add_item(self, description: str, due_date):
        self.item(description, due_date, self.status.pending, datetime.now())
        self.repo.create_item(self.item)

    def list_item(self):
        return self.repo.find_all_item()


    def remove_item(self, id):
        self.repo.remove_item(id)

    def remove_all(self):
        self.repo.remove_all()

# todo = todo_service_item()
# todo.add_item('hy', '10-11-1990')
# todo.add_item('hello', '05-12-2000')
# todo.list_item()






