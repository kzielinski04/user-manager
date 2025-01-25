import json
import os
import logging
import re

USERS_FILE = "users.json"

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handler
handler = logging.FileHandler("logs.log", encoding="utf-8", mode='w')

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Set formatter for handler
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

class User:
    """
    A class used to represent a User.
    
    Attributes:
    ----------------
    
    username : str
        name of the user

    email : str
        email address of the user

    role : str
        role of the user

    Methods:
    --------------

    get_data()
        retrieve user's data
    """
    
    def __init__(self, username: str, email: str, role: str):
        """Construct all the necessary attributes for the User object. 
        
        Parameters:
        ------------------

        username : str
            name of the user

        email : str
            email address of the user

        role : str
            role of the user
        """
        self.username = username
        self.email = email
        self.role = role

    def get_data(self) -> dict:
        """Retrieve user's data.

        Returns:
        -------------
        dict
            dict containing user's data
        """

        return {"username": self.username, "email": self.email, "role": self.role }

class UserManager:
    """A class used to manage users.
    
    Methods:
    --------------

    load_users()
        load users from file

    add_user()
        add new user to file

    remove_user()
        remove user from file
    
    display_users()
        display all users from file
    """

    def validate_email(email: str) -> bool:
        """Validate user's e-mail address

        Parameters:
        ------------------

        email : str
            user's e-mail address

        Returns:
        -------------

        bool
            true or false depending on whether the e-mail is valid
        """
        pattern = r"^.+@[A-Za-z]+\.[A-Za-z]+$"
        return True if re.match(pattern, email) else False

    def load_users() -> list:
            """Load users from file.
            
            Returns:
            -------------

            list
                list of users from file
            """
            if not os.path.exists(USERS_FILE):
                return []
            else:
                with open(USERS_FILE, 'r') as file:
                    try:
                        users = json.load(file)
                        return users
                    except json.JSONDecodeError:

                        logger.error("Nie udało się załadować danych użytkowników. Plik z użytkownikami jest uszkodzony.")
    
    def add_user(user: dict):
        """Add new user to file.

        Parameters:
        ------------------

        user : dict
            dict containing user's data
        """
        if not UserManager.validate_email(user["email"]):
            print("Adres e-mail użytkownika jest nieprawidłowy.\n")
            logger.error(f"Nie udało się dodać użytkownika o nazwie \"{user["username"]}\". Adres e-mail jest nieprawidłowy.")
            return
        users = UserManager.load_users()
        # if not users:
            # print("Wystąpił błąd. Plik z użytkownikami jest uszkodzony.\n")
            # logger.error("Plik z użytkownikami jest uszkodzony.")
            # return
        with open(USERS_FILE, 'w') as file:
            users.append(user)
            json.dump(users, file, indent=4)
            print(f"Pomyślnie dodano nowego użytkownika o nazwie \"{user["username"]}\".\n")
            logger.info(f"Dodano nowego użytkownika o nazwie \"{user["username"]}\".")

    def remove_user(username: str):
        """Remove user from file.
        
        Parameters:
        ------------------

        username : str
            name of the user

        """
        users = UserManager.load_users()
        # if not users:
            # print("Wystąpił błąd. Plik z użytkownikami jest uszkodzony.\n")
            # logger.error("Plik z użytkownikami jest uszkodzony.")
            # return
        updated_users = [u for u in users if u["username"] != username]
        if len(updated_users) != len(users):
            with open(USERS_FILE, 'w') as file:
                json.dump(updated_users, file, indent=4)
                print(f"Pomyślnie usunięto użytkownika o nazwie \"{username}\"\n")
                logger.info(f"Usunięto użytkownika o nazwie \"{username}\".")
        else:
            print(f"Nie znaleziono użytkownika o nazwie \"{username}\".\n")
            logger.error(f"Nie udało się usunąć użytkownika \"{username}\". Nie znaleziono w pliku użytkownika o takiej nazwie.")
            return

    def display_users():
        """Display all the users from file."""
        users = UserManager.load_users()
        if not users:
            print("Nie znaleziono żadnych użytkowników w pliku.\n")
            logger.error("Nie udało się wyświetlić użytkowników. Nie znaleziono żadnych użytkowników w pliku.")
            return
        else:
            for u in users:
                print(f"Nazwa użytkownika: \"{u["username"]}\" \t Adres e-mail: \"{u["email"]}\"\tRola: \"{u["role"]}\"")
                logger.info(f"Wyświetlono dane użytkownika \"{u["username"]}\".")
            print('\n')
            logger.info("Zakończono wyświetlanie danych użytkowników.")

def main():
    """Main loop."""
    logger.info("Program został uruchomiony.")
    while True:
        print("1 - Wyświetl użytkowników\n2 - Dodaj użytkownika\n3 - Usuń użytkownika\n4 - Wyjdź\n")
        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("Nieprawidłowy wybór.\n")
            continue
        if int(choice) not in {1, 2, 3, 4}:
            print("Nieprawidłowy wybór.\n")
            continue
        match choice:
            case 1:
                UserManager.display_users()
            case 2:
                username = input("Podaj nazwę użytkownika: ")
                email = input("Podaj adres e-mail: ")
                role = input("Podaj rolę: ")
                user = User(username, email, role)
                UserManager.add_user(user.get_data())
            case 3:
                username = input("Podaj nazwę użytkownika do usunięcia: ")
                UserManager.remove_user(username)
            case 4:
                logger.info("Zakończono działanie programu.")
                break

if __name__ == "__main__":
    main()