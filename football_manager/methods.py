from models import Team, Player
from sqlalchemy.orm import Session
from engine import engine


def create_team(name: str):
    session = Session(bind=engine)
    team = Team(name)
    session.add(team)
    session.commit()


def create_player(firstname: str, lastname: str, age: int, height: int, speed: int, team_id=None):
    session = Session(bind=engine)
    player = Player(firstname, lastname, age, height, speed, team_id)
    session.add(player)
    session.commit()


def get_all_teams():
    pass


def get_all_players():
    pass


def get_all_players_by_team(team):
    pass


def add_player_to_team(player, team):
    pass
