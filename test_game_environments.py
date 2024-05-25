"""
Environments:
- Login
- Lobby
- Play Bot -> 1v1
- Inventory
- Gambling -> Crates; Coins: Leveling Gyatts, PokeGyatt
"""
from test_user import User
from csv import DictReader


def check_exit(user_option):
    if user_option == 'exit':
        exit()


class Login:
    """
    Login environment which deals with creating a new user account
    or logging in to an existing user account.
    """

    @staticmethod
    def start_up() -> None:
        """
        First command to run on start, directs user to new account creation
        or current account login
        """

        # initial message on start up
        print("Greetings bozo, are you a new or existing player?")
        print("Type 'exit' to leave the game at any time.")

        # ask for valid input
        user_option: str = ''
        while user_option not in {'new', 'exist', 'exit'}:
            user_option = input("Choose 'new', 'exist': ").strip().lower()

        check_exit(user_option)

        # return contents of user info file
        with open('test_user_info.txt', 'r') as readfile:
            datas = [line for line in DictReader(readfile)]

            # redirect user to create new player or retrieve existing player details
            match user_option:
                case 'new':
                    Login.new_player(datas)
                case 'exist':
                    print("To be implemented")

    @staticmethod
    def new_player(file_info):
        """
        creates a new account using the user's inputted username and password
        :param file_info: contains all existing user's information
        """

        print()
        print('--- New Player Login ---')

        # only allow valid usernames
        print("Enter your username bozo (must be between 3 and 25 characters long, can only contain a-b and 0-9):")

        # taken usernames
        taken_usernames = [user['username'] for user in file_info]

        # ask for valid username
        username: str = ''
        while not (3 <= len(username) <= 25 and username.isalnum() and username not in taken_usernames):
            username = input("Choose a valid username: ").strip()
            check_exit(username)

        # only allow valid passwords
        print("Enter your password bozo (must be between 3 and 25 characters long):")

        # taken passwords
        taken_password = [user['password'] for user in file_info]

        # ask for valid password
        password: str = ''
        while not (3 <= len(password) <= 25 and password not in taken_usernames):
            password = input("Choose a valid password: ").strip()
            check_exit(password)

        player = User(username, password)
        print(player.__str__())


class Lobby:
    pass


if __name__ == '__main__':
    Login.start_up()

