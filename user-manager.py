import json
import os
import logging
import re

USERS_FILE = "users.json"

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
    """
    
    def __init__(self, username: str, email: str, role: str):
        """
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
        """Get user's data.

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

    def remove_user(username: str):
        users = UserManager.load_users()
        updated_users = [u for u in users if u["username"] != username]
        if len(updated_users) != len(users):
            with open(USERS_FILE, 'w') as file:
                json.dump(updated_users, file)
        else:
            raise Exception("User not found.")




# user1 = {"username": "abcd", "email": "abcd@gmail.com", "role": "user"}
# user2 = {"username": "efgh", "email": "efgh@gmail.com", "role": "user2"}

user = User("abcd", "email", "role")
user_data = user.get_data
UserManager.add_user(user_data)