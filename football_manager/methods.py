from datetime import datetime

from models import Team, Player


# flake8: noqa

def create_team(session, name: str):
    team = Team(name)
    session.add(team)
    session.commit()


def create_player(session, firstname: str, lastname: str, age: int, height: int, speed: int, team_id=None):
    player = Player(firstname, lastname, age, height, speed, team_id)
    session.add(player)
    session.commit()


def get_all_teams(session):
    teams = session.query(Team).filter().all()
    return teams


def get_all_team_names(teams):
    team_names = [teams.name for teams in teams]
    return team_names


def get_all_team_ids(teams):
    team_ids = [teams.id for teams in teams]
    return team_ids


def get_player_fullnames(players):
    all_player_fullnames = [player.firstname + ' ' + player.lastname for player in players]
    return all_player_fullnames


def get_all_players(session):
    players = session.query(Player).filter().all()
    return players


def get_all_players_ids(players):
    player_ids = [players.id for players in players]
    return player_ids


def get_all_players_by_team_id(session, team_id):
    players = session.query(Player).filter(Player.team_id == team_id).all()
    return players


def get_player_by_id(session, player_id):
    player = session.get(Player, player_id)

    return player


def get_team_by_id(session, team_id):
    team = session.get(Team, team_id)

    return team


def add_player_to_team(session, player, team):
    player.team_id = team.id
    session.commit()


# def remove_player_from_team(session, player, team):
#     player.team_id = None
#     change_team_updated_at()
#     change_players_amount()
#     session.commit()


def get_player_id_from_user():
    player_id = int(input('Enter player id: '))
    return player_id


def get_team_id_from_user():
    team_id = int(input('Enter team id: '))
    return team_id


def change_team_updated_at(session, team):  # переместить в метод класса как save
    team.updated_at = datetime.now()
    session.commit()


def change_players_amount(session, team, command):  # переместить в метод класса как plus_one minus_one
    if command == '+':
        team.players_amount += 1
    elif command == '-':
        team.players_amount -= 1
    elif command == 'all':
        team.players_amount = 0

    session.commit()


def get_records_amount(session, table):
    records_amount = session.query(table.id).count()
    return records_amount


def print_name_with_id(name_list, id_list):
    if len(name_list) > 0:
        for i in range(len(name_list)):
            print(f'{i + 1}. id - {id_list[i]}, name - {name_list[i]}')
    else:
        print('No data!')
