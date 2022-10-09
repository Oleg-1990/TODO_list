from Constants import constants as cons
from Repository import repository as repo
from TODO_item import todo_item
import utils
import json
import validators


class TodoServiceItem:
    def __init__(self):
        self.repo = repo.Repository()
        self.item = todo_item.TODO_item
        self.status = cons.status
        self.func = validators
        self.utils = utils

    def add_item(self, description: str, due_date):
        self.repo.create_item(self.item(description, due_date, self.status.pending, None))

    def add_a_few(self, *args):
        pass

    def list_item(self):
        return self.repo.find_all_item()

    def remove_item(self, id):
        self.repo.remove_item(id)

    def remove_all(self):
        self.repo.remove_all()

    def show_item(self, item: todo_item.TODO_item):
        return f'{item.description}, {self.utils.beautifull_date(item.due_date)}, {self.utils.color_of_status(item.status)}'

    def find_by_name(self, name):
        s = ''
        for todo in self.repo.find_by_name():
            if todo.description == name:
                s = f'Description: {todo.description}, Due date: {self.utils.beautifull_date(todo.due_date)}, ' \
                    f'Date_of_change: {self.utils.beautifull_date(todo.date_of_change)}, ' \
                    f'Status: {self.utils.color_of_status(todo.status)}'
        if s == '':
            return False
        else:
            return s

    def completed(self, id):
        self.repo.completed(id)

    def save_to_json(self):
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
                                                                          self.utils.computer_date(item['Due date']),
                                                                          item['Status'],
                                                                          self.utils.computer_date(
                                                                              item['Date_of_change'])))
            except:
                pass
