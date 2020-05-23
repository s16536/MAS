from datetime import date

from classes.user_group import UserGroup
from examples.mini_project_1 import print_banner
from classes.user import User, Address


def main():
    # zwykła asocjacja "* - *"

    # create sample users
    user_jan = User("jan_kowalski", "haslo123", "Jan", "Kowalski", date(1990, 4, 15),
                    Address("Dluga 18", "Warszawa", "Polska"))
    user_anna = User("anna_nowak", "mojeHaslo", "Jan", "Kowalski", date(2000, 3, 21),
                     Address("Backstreet 13", "Budapest", "Hungary"))

    # create group with two users
    user_group = UserGroup("psy", [user_jan, user_anna])

    print_banner("User Group links")
    user_group.print_links()

    print_banner("User Jan")
    user_jan.print_links()

    print_banner("User Anna")
    user_anna.print_links()

    group_koty = UserGroup("koty", [user_anna])

    print_banner("User Anna")
    user_anna.print_links()

    user_group.print_links()


if __name__ == '__main__':
    main()
