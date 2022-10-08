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
        self.service = todo_service.todo_service_item
        self.func = my_function

    def create_item(self, item) -> uuid.UUID:
        id = uuid.uuid4()
        self.DB_TODO[id] = item
        return id

    def remove_item(self, id: uuid.UUID):
        self.DB_TODO.pop(id)

    def remove_all(self):
        self.DB_TODO.clear()

    def find_all_item(self):
        return self.DB_TODO.items()

    def find_item(self, id: uuid.UUID):
        return self.DB_TODO[id]

    def completed(self, id):
        self.DB_TODO[id].status = colored(self.cons.status.completed, 'green')

    def canceled(self, id):
        self.DB_TODO[id].status = colored(self.cons.status.canceled, 'red')

    def save_to_json(self):
        with open('DB-TODO_list.json', 'w', encoding='utf-8') as file:
            lst = []
            for key, todo in self.DB_TODO.items():
                d = dict()
                d['ID'] = str(key)
                d['Description'] = todo.description
                d['Due date'] = self.func.beautifull_date(todo.due_date)
                d['Create date'] = self.func.beautifull_date(todo.creation_date)
                d['Status'] = todo.status
                lst.append(d)
            json.dump(lst, file)

    def read_from_json(self):
        with open('DB-TODO_list.json', 'r', encoding='utf-8') as file:
            lst = json.load(file)


    def find(self):
        print('Please enter name of the task you want to find')
        flag = False
        while not flag:
            name = input().strip().lower()
            for todo in self.DB_TODO.values():
                if todo.description == name:
                    print(f'Description: {todo.description}, Due date: {self.func.beautifull_date(todo.due_date)}, '
                          f'Create date: {self.func.beautifull_date(todo.creation_date)} Status: {todo.status}')
                    flag = True
            if not flag:
                print('name not found, try again')
