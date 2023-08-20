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
    def create(cls, session, team_name):
        team = Team(team_name)
        session.add(team)
        session.commit()

    def plus_player(self):
        self.players_amount += 1

    def minus_player(self):
        self.players_amount -= 1

    def save(self, session):
        self.updated_at = datetime.now()
        session.commit()

    def delete(self, session):
        self.is_active = False
        self.players = None
        self.players_amount = 0
        self.save(session)

    @staticmethod
    def get_all_active(session):
        teams = session.query(Team).filter(Team.is_active).all()
        return teams

    @staticmethod
    def get_by_id(session, team_id):
        team = session.get(Team, team_id)
        return team


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

    def __init__(self, firstname, lastname, age, height, speed, team):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.speed = speed
        self.team = team

    @classmethod
    def create(cls, session, firstname, lastname, age, height, speed, team_id=None):
        player = cls(firstname, lastname, age, height, speed, team_id)
        session.add(player)
        session.commit()

    def delete(self, session):
        self.is_active = False
        self.team = None
        session.commit()

    def remove_from_team(self):
        self.team = None

    @staticmethod
    def get_active(session):
        players = session.query(Player).filter(Player.is_active).all()
        return players

    @staticmethod
    def get_all_by_team(session, team):
        players = session.query(Player).filter(Player.team == team).all()
        return players

    @staticmethod
    def get_by_id(session, player_id):
        player = session.get(Player, player_id)
        return player

    @staticmethod
    def add_to_team(player, team):
        player.team = team
