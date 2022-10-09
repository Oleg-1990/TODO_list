import datetime
import uuid
import utils
from Constants import constants
import validators
import json


class Repository:
    def __init__(self):
        self.TASK_STORAGE = dict()
        self.cons = constants
        self.func = validators
        self.utils = utils

    def create_item(self, item):
        id = str(uuid.uuid4())
        self.TASK_STORAGE[id] = item
        return id

    def remove_item(self, id):
        self.TASK_STORAGE.pop(id)

    def remove_all(self):
        self.TASK_STORAGE.clear()

    def find_all_item(self):
        return self.TASK_STORAGE.items()

    def find_item(self, id):
        return self.TASK_STORAGE[id]

    def completed(self, id):
        self.TASK_STORAGE[id].status = self.utils.color_of_status('Completed')
        self.TASK_STORAGE[id].date_of_change = datetime.datetime.now()

    def canceled(self, id):
        self.TASK_STORAGE[id].status = self.utils.color_of_status('Canceled')
        self.TASK_STORAGE[id].date_of_change = datetime.datetime.now()

    def save_to_json(self):
        with open('DB-TODO_list.json', 'w', encoding='utf-8') as file:
            lst = []
            for key, todo in self.TASK_STORAGE.items():
                d = dict()
                d['ID'] = str(key)
                d['Description'] = todo.description
                d['Due date'] = self.utils.beautifull_date(todo.due_date)
                d['Date_of_change'] = self.utils.beautifull_date(todo.date_of_change)
                d['Status'] = todo.status
                lst.append(d)
            json.dump(lst, file)

    def create_item_from_json(self, id, item):
        self.TASK_STORAGE[id] = item

    def show_done_list(self):
        for todo in self.TASK_STORAGE.values():
            if todo.status == "Completed":
                print(f'{todo.description}, Date_of_done: {self.utils.beautifull_date(todo.date_of_change)},'
                      f' Status: {self.utils.color_of_status(todo.status)}')

    def find_by_name(self):
            return self.TASK_STORAGE.values()

