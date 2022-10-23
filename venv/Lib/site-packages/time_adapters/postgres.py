from arrow import Arrow
from psycopg2.extensions import adapt, register_adapter



register_adapter(
    Arrow,
    lambda x: adapt(x.to('UTC').naive)
)

# http://initd.org/psycopg/docs/advanced.html#adapting-new-python-types-to-sql-syntax
