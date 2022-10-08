import datetime


class TODO_item:
    def __init__(self, id, description: str, due_date: datetime, status: str, creation_date: datetime):
        self.id = id
        self.description = description
        self.due_date = due_date
        self.status = status
        self.creation_date = creation_date

