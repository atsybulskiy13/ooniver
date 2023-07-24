from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = 'team'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    players_amount: Mapped[int] = mapped_column(insert_default=0)
    created_at: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=datetime.now())

    def __init__(self, name):
        self.name = name


class Player(Base):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    age: Mapped[int]
    height: Mapped[int]
    speed: Mapped[int]
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"), nullable=True)

    def __init__(self, firstname, lastname, age, height, speed, team_id):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.speed = speed
        self.team_id = team_id
