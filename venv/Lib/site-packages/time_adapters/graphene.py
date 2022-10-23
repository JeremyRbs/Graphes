import graphene

from arrow import Arrow


PRECISION = 'second'



# create Graphene types, building on native types
class ArrowDate(graphene.types.Date):
    class Meta:
        name = "Date"

    @staticmethod
    def serialize(dt):
        if isinstance(dt, Arrow):
            dt = dt.date()

        return graphene.types.Date.serialize(dt)


class ArrowDateTime(graphene.types.DateTime):
    class Meta:
        name = "DateTime"

    @staticmethod
    def serialize(dt):
        if isinstance(dt, Arrow):
            dt = dt.floor(PRECISION).datetime

        return graphene.types.DateTime.serialize(dt)


# monkey patch graphene so that all Date / DateTime fields support arrow
# graphene.Date = ArrowDate
# graphene.DateTime = ArrowDateTime


try:
    from graphene_sqlalchemy.converter import convert_sqlalchemy_type
    from .sqlalchemy import ArrowType

    # register ArrowType with graphene
    @convert_sqlalchemy_type.register(ArrowType)
    def graphql_converter(type, column, registry=None):
        return ArrowDateTime

except ImportError:
    pass
