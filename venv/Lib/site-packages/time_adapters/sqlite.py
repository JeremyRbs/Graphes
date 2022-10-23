from arrow import Arrow
from sqlite3 import adapt, register_adapter



register_adapter(
    Arrow,
    lambda x: adapt(x.to('UTC').naive)
)

# https://docs.python.org/3.7/library/sqlite3.html#sqlite3.register_adapter
