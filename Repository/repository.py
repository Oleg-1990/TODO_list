import uuid
from Constants import constants
from termcolor import colored


class Repository:
    def __init__(self):
        self.DB_TODO = dict()
        self.cons = constants

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
        d = self.DB_TODO[id].status = colored(self.cons.status.completed, 'green')

    def canceled(self, id):
        d = self.DB_TODO[id].status = colored(self.cons.status.canceled, 'red')

