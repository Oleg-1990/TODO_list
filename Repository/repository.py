import datetime
import uuid
from Service import todo_service
from Constants import constants
from termcolor import colored
import my_function
import json


class Repository:
    def __init__(self):
        self.DB_TODO = dict()
        self.cons = constants
        self.service = todo_service.TodoServiceItem
        self.func = my_function

    def create_item(self, item):
        id = str(uuid.uuid4())
        self.DB_TODO[id] = item
        return id

    def remove_item(self, id):
        self.DB_TODO.pop(id)

    def remove_all(self):
        self.DB_TODO.clear()

    def find_all_item(self):
        return self.DB_TODO.items()

    def find_item(self, id):
        return self.DB_TODO[id]

    def completed(self, id):
        self.DB_TODO[id].status = colored(self.cons.status.completed, 'green')
        self.DB_TODO[id].date_of_change = datetime.datetime.now()

    def canceled(self, id):
        self.DB_TODO[id].status = colored(self.cons.status.canceled, 'red')
        self.DB_TODO[id].date_of_change = datetime.datetime.now()

    def save_to_json(self):
        with open('DB-TODO_list.json', 'w', encoding='utf-8') as file:
            lst = []
            for key, todo in self.DB_TODO.items():
                d = dict()
                d['ID'] = str(key)
                d['Description'] = todo.description
                d['Due date'] = self.func.beautifull_date(todo.due_date)
                d['Date_of_change'] = self.func.beautifull_date(todo.date_of_change)
                d['Status'] = todo.status
                lst.append(d)
            json.dump(lst, file)

    def create_item_from_json(self, id, item):
        self.DB_TODO[id] = item

    def show_done_list(self):
        for todo in self.DB_TODO.values():
            if todo.status == "\u001b[32mCompleted\u001b[0m":
                print(f'{todo.description}, Date_of_done: {self.func.beautifull_date(todo.date_of_change)},'
                      f' Status: {todo.status}')

    def find(self):
        print('Please enter name of the task you want to find')
        flag = False
        while not flag:
            name = input().strip().lower()
            for todo in self.DB_TODO.values():
                if todo.description == name:
                    print(f'Description: {todo.description}, Due date: {self.func.beautifull_date(todo.due_date)}, '
                          f'Date_of_change: {self.func.beautifull_date(todo.date_of_change)} Status: {todo.status}')
                    flag = True
            if not flag:
                print('name not found, try again')
