from datetime import datetime
from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = 'team'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    players_amount: Mapped[int] = mapped_column(Integer(), insert_default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=datetime.now())
    is_active: Mapped[bool] = mapped_column(insert_default=True)
    players: Mapped[List["Player"]] = relationship(back_populates="team")

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_team(cls, session, team_name):
        team = Team(team_name)
        session.add(team)
        session.commit()

    def plus_player(self):
        self.players_amount += 1

    def minus_player(self):
        self.players_amount -= 1

    def team_save(self, session):
        self.updated_at = datetime.now()
        session.commit()

    def delete_team(self):
        self.is_active = False
        self.players_amount = 0


class Player(Base):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String())
    lastname: Mapped[str] = mapped_column(String())
    age: Mapped[int] = mapped_column(Integer())
    height: Mapped[int] = mapped_column(Integer())
    speed: Mapped[int] = mapped_column(Integer())
    team_id: Mapped[int] = mapped_column(Integer(), ForeignKey("team.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, insert_default=True)
    team: Mapped['Team'] = relationship(back_populates="players")

    def __init__(self, firstname, lastname, age, height, speed, team_id):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.speed = speed
        self.team_id = team_id

    @classmethod
    def create_player(cls, session, firstname, lastname, age, height, speed, team_id=None):
        player = Player(firstname, lastname, age, height, speed, team_id)
        session.add(player)
        session.commit()

    def delete_player(self):
        self.is_active = False
        self.team_id = None

    def remove_player_from_team(self):
        self.team_id = None
