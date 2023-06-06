import os

from dotenv import load_dotenv

from ghost.authenticate import get_session_cookie


class GhostManager:
    """
    A class used to manage interactions with the Ghost client

    """

    def __init__(self):
        """
        Constructor

        Vars:
            cookie (str): Store session cookie

        """
        self.cookie = self.log_in()

    def log_in(self):
        """
        Gets credentials from .env to get session cookie

        Returns:
            cookie (str): Session cookie used to authenticate future requests

        """
    
        # Initial .env
        load_dotenv()

        # Obtain credentials
        username = os.getenv("GHOST_USERNAME")
        password = os.getenv("GHOST_PASSWORD")
        domain = os.getenv("GHOST_DOMAIN")

        # Get session cookie with credentials
        cookie = get_session_cookie(username, password, domain)

        return cookie

