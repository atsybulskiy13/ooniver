from models import Base, Team, Player
from sqlalchemy.orm import Session
from engine import engine
import methods
from menu import show_menu, get_user_option

Base.metadata.create_all(engine)


def main():
    session = Session(bind=engine)

    show_menu()

    user_option = get_user_option()

    if user_option != '10':

        match user_option:

            case '1':
                teams = methods.get_all_active_teams(session)

                team_names = methods.get_all_active_team_names(teams)
                all_team_ids = methods.get_all_active_team_ids(teams)

                print('Teams: ')
                methods.print_name_with_id(team_names, all_team_ids)

            case '2':
                all_players = methods.get_all_active_players(session)

                all_players_fullnames = methods.get_player_fullnames(all_players)
                all_player_ids = methods.get_all_active_players_ids(all_players)

                print('Players: ')
                methods.print_name_with_id(all_players_fullnames, all_player_ids)

            case '3':
                players_without_team = methods.get_all_active_players_by_team_id(session, None)

                players_without_team_fullnames = methods.get_player_fullnames(players_without_team)
                players_without_team_ids = methods.get_all_active_players_ids(players_without_team)

                print('Players without team: ')
                methods.print_name_with_id(players_without_team_fullnames, players_without_team_ids)

            case '4':
                team_name = input('Enter new team name: ')

                Team.create_team(session, team_name)

            case '5':
                player_firstname = input("Enter player's firstname: ")
                player_lastname = input("Enter player's lastname: ")
                player_age = int(input("Enter player's age: "))
                player_height = int(input("Enter player's height: "))
                player_speed = int(input("Enter player's speed: "))

                Player.create_player(session, player_firstname, player_lastname, player_age, player_height,
                                     player_speed)

            case '6':
                player_id = methods.get_player_id_from_user()
                team_id = methods.get_team_id_from_user()

                player = methods.get_player_by_id(session, player_id)
                team = methods.get_team_by_id(session, team_id)

                methods.add_player_to_team(player, team)

                team.plus_player()
                team.team_save(session)

            case '7':
                player_id = methods.get_player_id_from_user()

                player = methods.get_player_by_id(session, player_id)
                team = player.team

                player.remove_player_from_team()

                team.minus_player()
                team.team_save(session)

            case '8':
                team_id = methods.get_team_id_from_user()
                team = methods.get_team_by_id(session, team_id)

                if team.players:
                    for player in team.players:
                        player.team_id = None

                team.delete_team()
                team.team_save(session)

            case '9':
                player_id = methods.get_player_id_from_user()
                player = methods.get_player_by_id(session, player_id)

                if player.team_id is not None:
                    team = methods.get_team_by_id(session, player.team_id)
                    team.minus_player()
                    team.team_save(session)

                player.delete_player()
                session.commit()

        main()

    else:
        print('Program finished!')


if __name__ == '__main__':
    main()
