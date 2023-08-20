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
