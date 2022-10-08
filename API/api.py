from Service import todo_service
from datetime import datetime
import function


class Api:
    def __init__(self):
        self.service = todo_service.todo_service_item()
        self.tasks = self.service.list_item() # return list[tuple(key,value)]
        self.func = function

    def add(self):
        print('Please enter task')
        task = input().strip()
        due_date = self.func.validate_date()
        print('Please enter due date in format dd.mm.yyyy')
        self.service.add_item(task, due_date)

    def list(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            print('It`s all list tasks')
            for task in enumerate(self.tasks, 1):
                print(task[0], task[1][1])

    def help(self):
        print('Commands:', end=' ')
        for fanc in dir(self):
            if not fanc.startswith('__'):
                print("'" + fanc + "'", end=' ')
        print()

    def remove(self):
        if len(self.tasks) == 0:
            print('You don`t add any tasks')
        else:
            for task in enumerate(self.tasks, 1):
                print(task[0], task[1][1])
            print('Please enter index task, what do you want to remove')
            index = int(input().strip())-1
            id = list(self.tasks)[index][0]
            self.service.remove_item(id)

    def remove_all(self):
        self.service.remove_all()

    def exit(self):
        return True
