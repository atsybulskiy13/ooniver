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


def get_all_team_names(session):
    team_names = session.query(Team.name).all()
    team_names = [name[0] for name in team_names]
    return team_names


def get_player_fullnames(players):
    all_player_fullnames = [player.firstname + ' ' + player.lastname for player in players]
    return all_player_fullnames


# спросить на занятии!!!!

def get_all_players(session):
    players = session.query(Player).filter().all()
    return players


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


def remove_player_from_team(session, player):
    player.team_id = None
    session.commit()


def get_records_amount(session, table):
    records_amount = session.query(table.id).count()
    return records_amount


def print_name(name_list):
    if len(name_list) > 0:
        for i in range(len(name_list)):
            print(f'{i + 1}. {name_list[i]}')
    else:
        print('No data!')
