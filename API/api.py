from Service import todo_service
import validators
from datetime import datetime


class Api:
    def __init__(self):
        self.service = todo_service.TodoServiceItem()
        self.tasks = self.service.list_item()

    def add(self):
        flag = False
        due_date = ''
        print('Please enter task')
        task = input().strip().lower()
        print('Please enter due date in format dd.mm.yyyy')
        while not flag:
            due_date = validators.validate_date(input())
            if isinstance(due_date, datetime):
                self.service.add_item(task, due_date)
                flag = True
            else:
                print('You entered an invalid date, please try again in format dd.mm.yyyy.')


    def add_a_few(self):
        pass

    def list(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            print('It`s all list tasks')
            for task in enumerate(self.tasks, 1):
                print(task[0], self.service.show_item(task[1][1]))

    def help(self):
        print('Commands:', end=' ')
        for fanc in dir(self):
            if not fanc.startswith('__') and fanc != 'service' and fanc != 'tasks' and fanc != 'read_file':
                print("'" + fanc + "'", end=' ')
        print()

    def remove(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            for task in enumerate(self.tasks, 1):
                print(task[0], self.service.show_item(task[1][1]))
            print('Please enter index task, what do you want to remove')
            index = validators.valid_index(len(self.tasks))
            id = list(self.tasks)[index - 1][0]
            self.service.remove_item(id)

    def completed(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            for task in enumerate(self.tasks, 1):
                print(task[0], self.service.show_item(task[1][1]))
            print('Please enter index task to completed')
            index = validators.valid_index(len(self.tasks))
            id = list(self.tasks)[index - 1][0]
            self.service.completed(id)

    def canceled(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            for task in enumerate(self.tasks, 1):
                print(task[0], self.service.show_item(task[1][1]))
            print('Please enter index task to canceled')
            index = validators.valid_index(len(self.tasks))
            id = list(self.tasks)[index - 1][0]
            self.service.canceled(id)

    def find(self):
        print('Please enter name of the task you want to find')
        flag = False
        while not flag:
            name = input().strip().lower()
            tmp = self.service.find_by_name(name)
            if isinstance(tmp, str):
                print(tmp)
                flag = True
            else:
                print('name not founded, try again')


    def remove_all(self):
        self.service.remove_all()

    def exit(self):
        self.service.save_to_json()

    def read_file(self):
        self.service.read_file()

    def done_list(self):
        self.service.done_list()
