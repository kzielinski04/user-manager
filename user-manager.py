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
            dictionary containing user's data
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

    validate_email()
        validate user's e-mail address
    
    validate_username()
        validate user's name

    validate_role()
        validate user's role
   
    check_user()
        check if user already exists in file
     """

    @staticmethod
    def check_user(username: str) -> bool:
        """"Check if user already exists in file.

        Parameters:
        -------------------

        username : str
            name of the user

        Returns:
        -------------

        bool
            true or false depending or whether user already exists in file or not 
        """
        try:
            users = UserManager.load_users()
            usernames = {user["username"] for user in users}
            return True if username in usernames else False
        except Exception:
            raise Exception

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate user's e-mail address

        Parameters:
        ------------------

        email : str
            user's e-mail address

        Returns:
        -------------

        bool
            true or false depending on whether the e-mail is valid or not
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, email) else False

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate user's name.
        
        Parameters:
        ------------------

        username : str
            user's name

        Returns:
        -------------

        bool
            true or false depending on whether the username is valid or not
        """

        return True if len(username.strip()) > 0 else False

    @staticmethod
    def validate_role(role: str) -> bool:
        """Validate user's role.
        
        Parameters:
        -------------------

        role : str
            user's role

        Returns:
        -------------

        bool
            true or false depending or whether the role is valid or not
        """

        return True if len(role.strip()) > 0 else False

    @staticmethod
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
                        raise Exception
    
    @staticmethod
    def add_user(user: dict):
        """Add new user to file.

        Parameters:
        ------------------

        user : dict
            dict containing user's data
        """
        try:
            users = UserManager.load_users()
        except Exception:
            print("Wystąpił błąd. Plik z użytkownikami jest uszkodzony.\n")
            logger.error("Plik z użytkownikami jest uszkodzony.")
            logger.error("Nie udało się dodać użytkownika.")
            return
        
        with open(USERS_FILE, 'w') as file:
            users.append(user)
            json.dump(users, file, indent=4)
            print(f"Pomyślnie dodano nowego użytkownika o nazwie \"{user["username"]}\".\n")
            logger.info(f"Dodano nowego użytkownika o nazwie \"{user["username"]}\".")

    @staticmethod
    def remove_user(username: str):
        """Remove user from file.
        
        Parameters:
        ------------------

        username : str
            name of the user

        """
        try:
            users = UserManager.load_users()
        except Exception:
            print("Wystąpił błąd. Plik z użytkownikami jest uszkodzony.\n")
            logger.error("Plik z użytkownikami jest uszkodzony.")
            logger.error("Nie udało się usunąć użytkownika.")
            return
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

    @staticmethod
    def display_users():
        """Display all the users from file."""
        try:
            users = UserManager.load_users()
        except Exception:
            print("Wystąpił błąd. Plik z użytkownikami jest uszkodzony.\n")
            logger.error("Plik z użytkownikami jest uszkodzony.")
            logger.error("Nie udało się wyświetlić danych użytkowników.")
            return
        
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
        
        # Validate choice
        except ValueError:
            print("Nieprawidłowy wybór.\n")
            logger.error(f"Wprowadzony wybór \"{choice}\"jest nieprawidłowy. Wprowadzono znak, który nie jest liczbą całkowitą.")
            continue
        if int(choice) not in {1, 2, 3, 4}:
            print("Nieprawidłowy wybór.\n")
            logger.error(f"Wprowadzony wybór \"{choice}\" jest nieprawidłowy. Wybrano liczbę całkowitą spoza zakresu (1-4).")
            continue

        match choice:
            case 1:
                logger.info("Wybrano opcję wyświetlenia danych użytkowników.")
                UserManager.display_users()

            # Add user
            case 2:
                logger.info("Wybrano opcję dodania nowego użytkownika.")
                try:
                    username = input("Podaj nazwę użytkownika: ")
                    logger.debug(f"Wprowadzono nazwę użytkownika: \"{username}\".")

                    # Validate username
                    if not UserManager.validate_username(username):
                        print("Nazwa użytkownika jest nieprawidłowa. Nazwa użytkownika musi się składać z co najmniej jednego znaku.\n")
                        logger.error(f"Walidacja wprowadzonej nazwy użytkownika \"{username}\" nie przebiegła pomyślnie.")
                        logger.error(f"Nie udało się dodać użytkownika.")
                        continue
                    logger.debug(f"Walidacja wprowadzonej nazwy użytkownika \"{username}\" przebiegła pomyślnie.")

                    # Check if user already exists in file
                    if UserManager.check_user(username):
                        print(f"Nie udało się dodać użytkownika. Użytkownik o nazwie \"{username}\"  już istnieje w pliku.\n")
                        logger.error(f"Nie udało się dodać użytkownika. Użytkownik o nazwie \"{username}\" już istnieje w pliku.")
                        continue

                    email = input("Podaj adres e-mail: ")
                    logger.debug(f"Wprowadzono adres e-mail użytkownika: \"{email}\".")
                    
                    # Validate e-mail address
                    if not UserManager.validate_email(email):
                        print("Wprowadzony adres e-mail jest nieprawidłowy.\n")
                        logger.error(f"Walidacja wprowadzonego adresu e-mail \"{email}\" nie przebiegła pomyślnie.")
                        logger.error(f"Nie udało się dodać użytkownika o nazwie \"{username}\".")
                        continue
                    logger.debug(f"Walidacja wprowadzonego adresu e-mail \"{email}\" przebiegła pomyślnie.")
                    
                    role = input("Podaj rolę: ")
                    logger.debug(f"Wprowadzono rolę użytkownika: \"{role}\".")

                    # Validate role
                    if not UserManager.validate_role(role):
                        print("Nazwa roli użytkownika jest nieprawidłowa. Nazwa musi składać się conajmniej z jednego znaku.\n")
                        logger.error(f"Walidacja wprowadzonej roli \"{role}\" nie przebiegła pomyślnie.")
                        logger.error(f"Nie udało się dodać użytkownika o nazwie: \"{username}\".")
                        continue
                    logger.debug(f"Walidacja wprowadzonej roli \"{role}\" przebiegła pomyślnie.")
                    
                    # Create User object
                    user = User(username, email, role)
                    logger.info(f"Utworzono obiekt klasy User z danymi: username: \"{username}\"; email: \"{email}\"; role: \"{role}\".")
                    UserManager.add_user(user.get_data())
                except Exception:
                    print("Nie udało się dodać użytkownika. Plik z użytkownikami jest uszkodzony.\n")
                    logger.error(f"Nie udało się dodać użytkownika o nazwie \"{username}\". Plik z użytkownikami jest uszkodzony.")
                    continue
            
            # Remove user
            case 3:
                logger.info("Wybrano opcję usunięcia użytkownika.")
                username = input("Podaj nazwę użytkownika do usunięcia: ")
                logger.info(f"Wprowadzono nazwę użytkownika do usunięcia: \"{username}\"")

                # Validate username
                if not UserManager.validate_username(username):
                    print("Nazwa użytkownika jest nieprawidłowa. Nazwa użytkownika musi się składać z conajmniej jednego znaku.\n")
                    logger.error(f"Walidacja wprowadzonej nazwy użytkownika \"{username}\" nie przebiegła pomyślnie. Nazwa użytkownika nie składa się z co najmniej jednego znaku.")
                    logger.error(f"Nie udało się usunąć użytkownika o nazwie \"{username}\".")
                    continue
                logger.debug(f"Walidacja wprowadzonej nazwy użytkownika \"{username}\" przebiegła pomyślnie.")
                UserManager.remove_user(username)

            # Exit program
            case 4:
                logger.info("Wybrano opcję wyjścia z programu.")
                logger.info("Zakończono działanie programu.")
                break

if __name__ == "__main__":
    main()