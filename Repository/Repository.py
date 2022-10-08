import uuid

from TODO_item import TODO_item


class Repository:
    def __init__(self):
        self.DB_TODO = dict()

    def create_item(self, item: TODO_item) -> uuid.UUID:
        id = uuid.uuid4()
        self.DB_TODO[id] = item
        return id

    def delete_item(self, id: uuid.UUID):
        self.DB_TODO.pop(id)

    def find_all_item(self) -> list:
        return list(self.DB_TODO.values())

    def find_item(self, id: uuid.UUID):
        return self.DB_TODO[id]


