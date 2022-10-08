from Constants import constants as cons
from Repository import repository as repo
from TODO_item import todo_item
from datetime import datetime
from termcolor import colored
import my_function

class todo_service_item:
    def __init__(self):
        self.repo = repo.Repository()
        self.item = todo_item.TODO_item
        self.status = cons.status
        self.func = my_function

    def add_item(self, description: str, due_date):
        self.repo.create_item(self.item(description, due_date, colored(self.status.pending, 'yellow'), datetime.now()))

    def list_item(self):
        return self.repo.find_all_item()

    def remove_item(self, id):
        self.repo.remove_item(id)

    def remove_all(self):
        self.repo.remove_all()

    def show_item(self, item: todo_item.TODO_item):
        return f'{item.description}, {self.func.beautifull_date(item.due_date)}, {item.status}'

    def find(self):
        self.repo.find()

    def completed(self, id):
        self.repo.completed(id)

    def exit(self):
        self.repo.save_to_json()

    def canceled(self, id):
        self.repo.canceled(id)

    def read_file(self):
        self.repo.read_from_json()


