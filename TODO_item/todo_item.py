import datetime


class TODO_item:
    def __init__(self, description: str, due_date: datetime, status: str, date_of_change: datetime):
        self.description = description
        self.due_date = due_date
        self.status = status
        self.date_of_change = date_of_change
