from Constants import constants as cons
from Repository import repository as repo
from TODO_item import todo_item
from datetime import datetime
from termcolor import colored
import json
import my_function


class TodoServiceItem:
    def __init__(self):
        self.repo = repo.Repository()
        self.item = todo_item.TODO_item
        self.status = cons.status
        self.func = my_function

    def add_item(self, description: str, due_date):
        self.repo.create_item(self.item(description, due_date, colored(self.status.pending, 'yellow'), None))

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

    def done_list(self):
        self.repo.show_done_list()


    def read_file(self):
        with open('DB-TODO_list.json', 'r', encoding='utf-8') as file:
            try:
                lst = json.load(file)
                for item in lst:
                    self.repo.create_item_from_json(item["ID"], self.item(item['Description'],
                                                                      self.func.computer_date(item['Due date']),
                                                                      item['Status'],
                                                                     self.func.computer_date(item['Date_of_change'])))
            except:
                pass