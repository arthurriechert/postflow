import requests

def get_session_cookie(username, password, domain):
    """
    Give user access to Ghost Admin API
    Admin API will store cookie for login.

    Args:
        username (str): Contain user's email or username
        password (str): Stores users password
        domain (str): Domain name without extension

    Returns:
        cookie (str): Cookie used to authenticate future requests
    
    """

    # Create new session
    session = requests.Session()

    # Set up header
    headers = {
        "Origin": "http://localhost",
        "Accept-Version": "v5.0",
        "Content-Type": "application/json"
    }

    # Set up user credentials
    data = {
        'username': username,
        'password': password
    }

    # Send POST request for login
    cookie = session.post(f"https://{domain}.ghost.io/ghost/api/admin/session/", headers=headers, json=data)

    # Check status code
    if cookie.status_code == 201:
        print("\n\033[32mSession created successfully\033[0m")
    else:
        print(f"\n\033[31mFailed to create session. STATUS CODE: {cookie.status_code}\033[0m")

    return session, headers
