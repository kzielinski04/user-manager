import json
import os
import logging
import re

class User:
    """
    A class used to represent a User.
    
    Attributes:
    -------------------------
    
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
        -------------------------

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