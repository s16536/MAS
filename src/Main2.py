from ObjectPlus import ObjectPlus
from User import User


def main():
    ObjectPlus.load_extents()
    user1 = User.get_extent()
    print(user1)

if __name__ == '__main__':
    main()