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


# user1 = {"username": "abcd", "email": "abcd@gmail.com", "role": "user"}
# user2 = {"username": "efgh", "email": "efgh@gmail.com", "role": "user2"}
# 
# UserManager.add_user(user2)