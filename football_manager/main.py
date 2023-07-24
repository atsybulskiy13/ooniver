# from sqlalchemy.orm import Session

from models import Base

from engine import engine
from methods import create_team, create_player


Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_team('Manchester')
    create_team('Barselona')

    create_player('Sasha', 'Tsyb', 22, 190, 20)
    create_player('Denero', 'Cvach', 22, 180, 15)
