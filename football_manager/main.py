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
                teams = Team.get_all_active(session)

                team_names = [teams.name for teams in teams]
                team_ids = [teams.id for teams in teams]

                print('Teams: ')
                methods.print_name_with_id(team_names, team_ids)

            case '2':
                active_players = Player.get_active(session)

                players_fullnames = [player.firstname + ' ' + player.lastname for player in active_players]
                player_ids = [players.id for players in active_players]

                print('Players: ')
                methods.print_name_with_id(players_fullnames, player_ids)

            case '3':
                players_without_team = Player.get_all_by_team(session, None)

                players_fullnames = [player.firstname + ' ' + player.lastname for player in players_without_team]
                players_ids = [players.id for players in players_without_team]

                print('Players without team: ')
                methods.print_name_with_id(players_fullnames, players_ids)

            case '4':
                team_name = input('Enter new team name: ')

                Team.create(session, team_name)

            case '5':
                player_firstname = input("Enter player's firstname: ")
                player_lastname = input("Enter player's lastname: ")
                player_age = int(input("Enter player's age: "))
                player_height = int(input("Enter player's height: "))
                player_speed = int(input("Enter player's speed: "))

                Player.create(session, player_firstname, player_lastname, player_age, player_height,
                              player_speed)

            case '6':
                player_id = methods.get_player_id_from_user()
                team_id = methods.get_team_id_from_user()

                player = Player.get_by_id(session, player_id)
                team = Team.get_by_id(session, team_id)

                Player.add_to_team(player, team)

                team.plus_player()
                team.save(session)

            case '7':
                player_id = methods.get_player_id_from_user()

                player = Player.get_by_id(session, player_id)
                team = player.team

                player.remove_from_team()

                team.minus_player()
                team.save(session)

            case '8':
                team_id = methods.get_team_id_from_user()
                team = Team.get_by_id(session, team_id)

                if team.players:
                    for player in team.players:
                        player.team_id = None

                team.delete()

            case '9':
                player_id = methods.get_player_id_from_user()
                player = Player.get_by_id(session, player_id)

                if player.team_id is not None:
                    team = Team.get_by_id(session, player.team_id)
                    team.minus_player()
                    team.save(session)

                player.delete()

        main()

    else:
        print('Program finished!')


if __name__ == '__main__':
    main()
