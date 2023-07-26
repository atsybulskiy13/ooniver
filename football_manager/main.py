# from sqlalchemy.orm import Session
# flake8: noqa
from models import Base
# from models import Player, Team
from sqlalchemy.orm import Session
from engine import engine
from methods import *
from menu import *

Base.metadata.create_all(engine)


def main():
    session = Session(bind=engine)

    show_menu()

    user_option = get_user_option()

    if user_option != '9':

        match user_option:

            case '1':
                team_names = get_all_team_names(session)

                print('Teams: ')
                print_name(team_names)

            case '2':
                all_players = get_all_players(session)
                all_players_fullnames = get_player_fullnames(all_players)

                print('Players: ')
                print_name(all_players_fullnames)

            case '3':
                players_without_team = get_all_players_by_team_id(session, None)
                players_without_team_fullnames = get_player_fullnames(players_without_team)

                print('Players without team: ')
                print_name(players_without_team_fullnames)

            case '4':
                team_name = input('Enter new team name: ')
                create_team(session, team_name)

            case '5':
                player_firstname = input("Enter player's firstname: ")
                player_lastname = input("Enter player's lastname: ")
                player_age = int(input("Enter player's age: "))
                player_height = int(input("Enter player's height: "))
                player_speed = int(input("Enter player's speed: "))

                create_player(session, player_firstname, player_lastname, player_age, player_height, player_speed)

            case '6':
                pass

            case '7':
                pass

            case '8':
                pass
        main()

    else:
        print('Program finished!')


if __name__ == '__main__':
    main()
