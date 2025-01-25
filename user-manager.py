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
    
    """

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
                    users = json.load(file)
                    return users
    
    def add_user(user: dict):
        """Add new user to file.

        Parameters:
        ------------------

        user : dict
            dict containing user's data
        """
        users = UserManager.load_users()
        with open(USERS_FILE, 'w') as file:
            users.append(user)
            json.dump(users, file, indent=4)
            logger.info(f"Dodano nowego użytkownika o nazwie \"{user["username"]}\".")

    def remove_user(username: str):
        """Remove user from file.
        
        Parameters:
        ------------------

        username : str
            name of the user

        """
        users = UserManager.load_users()
        updated_users = [u for u in users if u["username"] != username]
        if len(updated_users) != len(users):
            with open(USERS_FILE, 'w') as file:
                json.dump(updated_users, file, indent=4)
                print(f"Pomyślnie usunięto użytkownika o nazwie \"{username}\"")
                logger.info(f"Usunięto użytkownika o nazwie \"{username}\".")
        else:
            print(f"Nie znaleziono użytkownika o nazwie \"{username}\".")
            logger.error(f"Nie udało się usunąć użytkownika \"{username}\". Nie znaleziono w pliku użytkownika o takiej nazwie.")
            return

    def display_users():
        """Display all the users from file."""
        users = UserManager.load_users()
        if not users:
            print("Nie znaleziono żadnych użytkowników w pliku.")
            logger.error("Nie udało się wyświetlić użytkowników. Nie znaleziono żadnych użytkowników w pliku.")
            return
        else:
            for u in users:
                print(f"Nazwa użytkownika: \"{u["username"]}\" \t Adres e-mail: \"{u["email"]}\"\tRola: \"{u["role"]}\"")
                logger.info(f"Wyświetlono dane użytkownika \"{u["username"]}\".")
            logger.info("Zakończono wyświetlanie danych użytkowników.")

# user1 = User("abcd", "abcd@gmail.com", "role1")
# UserManager.add_user(user1.get_data())
# user2 = User("efgh", "efgh@gmail.com", "role2")
# UserManager.add_user(user2.get_data())
# user3 = User("1234", "1234@gmail.com", "role3")
# UserManager.add_user(user3.get_data())
# user4 = User("xyzv", "xyzv@gmail.com", "role4")
# UserManager.add_user(user4.get_data())
# 
# 
# 
# 
# 
# UserManager.display_users()

# UserManager.remove_user("1234")