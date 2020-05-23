from classes.user_group import UserGroup
from object_plus.object_plus import ObjectPlus
from classes.user import User


def main():
    ObjectPlus.load_extents()
    user1 = User.get_extent()[0]

    userGroup = UserGroup("psy", [user1])

    userGroup.print_links("user")
    userGroup.print_links()
    user1.print_links()


if __name__ == '__main__':
    main()
