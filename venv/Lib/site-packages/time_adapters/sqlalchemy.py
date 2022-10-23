import arrow
from sqlalchemy.types import TypeDecorator, TIMESTAMP



class ArrowType(TypeDecorator):
    '''
    Timestamp that is saved and loaded with UTC timezone.
    '''

    impl = TIMESTAMP
    DEFAULT_PRECISION = 'microsecond'
    DEFAULT_TZ = 'local'


    def __init__(self, precision=None, tz=None, *args, **kwargs):
        self.precision = precision or self.DEFAULT_PRECISION
        self.tz = tz or self.DEFAULT_TZ
        super(ArrowType, self).__init__(*args, **kwargs)


    def coerce(self, value):
        return arrow.get(value).floor(self.precision).to(self.tz)


    def process_bind_param(self, value, dialect):
        if value:
            # convert to UTC before saving to db
            return self.coerce(value).to('UTC').naive
            # return utc_val.datetime if self.impl.timezone else utc_val.naive

        return value


    def process_result_value(self, value, dialect):
        # load value from db and add UTC timezone
        if value:
            value = self.coerce(value)

        return value


    @property
    def python_type(self):
        return self.impl.type.python_type



# Thanks to sqlalchemy-utils
# https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/arrow.html#ArrowType
# https://docs.sqlalchemy.org/en/13/core/custom_types.html#typedecorator-recipes
