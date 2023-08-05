from models import Team, Player


def get_all_active_teams(session):
    teams = session.query(Team).filter(Team.is_active).all()
    return teams


def get_all_active_team_names(teams):
    team_names = [teams.name for teams in teams]
    return team_names


def get_all_active_team_ids(teams):
    team_ids = [teams.id for teams in teams]
    return team_ids


def get_player_fullnames(players):
    all_player_fullnames = [player.firstname + ' ' + player.lastname for player in players]
    return all_player_fullnames


def get_all_active_players(session):
    players = session.query(Player).filter(Player.is_active).all()
    return players


def get_all_active_players_ids(players):
    player_ids = [players.id for players in players]
    return player_ids


def get_all_active_players_by_team_id(session, team_id):
    players = session.query(Player).filter(Player.team_id == team_id).all()
    return players


def get_player_by_id(session, player_id):
    player = session.get(Player, player_id)

    return player


def get_team_by_id(session, team_id):
    team = session.get(Team, team_id)

    return team


def add_player_to_team(player, team):
    player.team_id = team.id


def get_player_id_from_user():
    player_id = int(input('Enter player id: '))
    return player_id


def get_team_id_from_user():
    team_id = int(input('Enter team id: '))
    return team_id


def print_name_with_id(name_list, id_list):
    if len(name_list) > 0:
        for i in range(len(name_list)):
            print(f'{i + 1}. id - {id_list[i]}, name - {name_list[i]}')
    else:
        print('No data!')
