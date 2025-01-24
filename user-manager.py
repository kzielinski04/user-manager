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
