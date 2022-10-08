from collections import namedtuple

Status = namedtuple('Status', ['pending', 'complete', 'canceled'])
status = Status('Pending', 'Complete', 'Canceled')

