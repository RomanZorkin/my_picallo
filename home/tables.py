from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, Text


class Task(Table):
    """
    An example table.
    """

    name = Varchar()
    completed = Boolean(default=False)


class Endpoint(Table):
    
    clubid = Text()
    login = Text()
    password = Text()
    url = Text()
