from classes.user_group import UserGroup
from examples.mini_project_1 import print_banner
from object_plus.object_plus import ObjectPlus
from classes.user import User


def main():
    ObjectPlus.load_extents()
    user1 = User.get_extent()[0]

    user_group = UserGroup("psy", [user1])

    print_banner("User Group links")
    user_group.print_links()

    print_banner("User links")
    user1.print_links()


if __name__ == '__main__':
    main()
