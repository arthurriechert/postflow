import os

from dotenv import load_dotenv

from ghost.authenticate import get_session_cookie
import ghost.content as content

class GhostManager:
    """
    A class used to manage interactions with the Ghost client

    """

    def __init__(self):
        """
        Constructor

        Vars:
            session (str): Store instance of requests.Session
            header (json): Important information for interacting with Ghost API

        """
        self.session, self.headers = self.log_in()

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

        # Get session with credentials
        session, headers = get_session_cookie(username, password, domain)

        return session, headers

