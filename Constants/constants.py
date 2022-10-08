from collections import namedtuple

Status = namedtuple('Status', ['pending', 'completed', 'canceled'])
status = Status('Pending', 'Completed', 'Canceled')

