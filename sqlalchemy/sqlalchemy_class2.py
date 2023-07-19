from sqlalchemy import create_engine, Table, Column, \
    Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship


class LibraryUser:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Address:
    def __init__(self, user, email):
        self.user = user
        self.email = email


engine = create_engine("sqlite:///library1.db", echo=True)
mapper_registry = registry()

user_table = Table(
    'LibraryUser',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('firstname', String, nullable=False),
    Column('lastname', String),
)

address = Table(
    "address",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("LibraryUser.id")),
    Column("email_address", String(50)),
)

mapper_registry.map_imperatively(
    LibraryUser,
    user_table,
    properties={
        "addresses": relationship(Address, backref="user", order_by=address.c.id)
    },
)

mapper_registry.map_imperatively(Address, address)

mapper_registry.metadata.create_all(engine)
