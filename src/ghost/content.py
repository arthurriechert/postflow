from parse import parse_json, flatten, remove_duplicate_elements
import json as js

def get_post(slug: str, session, headers, domain: str):
    """
    Obtains content from a ghost page
    
    Args:
        session (Session): Verified session instance
        slug (str): Page name
        headers (json): Important information for getting requests
        domain (str): Domain of the ghost blog, excluding .ext

    Returns:
        data (json): Data from the page

    """

    # Build URL with slug
    url = f"https://{domain}.ghost.io/ghost/api/admin/posts/slug/{slug}"

    # Get the post
    post = session.get(url, headers=headers)

    # Print post
    print(f"""
    ########## RETRIEVED POST ##########

    STATUS CODE: {post.status_code}

    {post.json()}""")

def get_slugs(session, headers, domain: str):
    """
    Gets a list of slugs to send to ChatGPT

    Args:
        session (Session): Verified session instance
        headers (json): Important information for getting requests
        domain (str): Domain of the ghost blog, excluding .ext

    Returns:
        slugs (dict): List containing slugs
    
    """

    # URL endpoint to get posts
    url = f"https://{domain}.ghost.io/ghost/api/admin/posts"

    # Get JSON with post information
    posts = session.get(url, headers=headers)

    # Parse out the slugs
    slugs = parse_json(posts.json(), "slug")

    # Flatten list of slugs
    slugs = flatten(slugs)

    # Remove duplicates
    slugs = remove_duplicate_elements(slugs)

    # Print posts' metadata
    print(f"""
    ########## SLUGS  ##########
    {slugs}""")
    
    return slugs

def get_titles(session, headers, domain: str):
    """
    Gets a list of titles to send to ChatGPT

    Args:
        session (Session): Verified session instance
        headers (json): Important information for getting requests
        domain (str): Domain of the ghost blog, excluding .ext

    Returns:
        titles (dict): List containing slugs
    
    """

    # URL endpoint to get posts
    url = f"https://{domain}.ghost.io/ghost/api/admin/posts"

    # Get JSON with post information
    posts = session.get(url, headers=headers)

    # Parse out the slugs
    titles = parse_json(posts.json(), "title")

    # Flatten list of slugs
    titles = flatten(titles)

    # Remove duplicates
    titles = remove_duplicate_elements(titles)

    # Print posts' metadata
    print(f"""
    ########## TITLES  ##########
    {titles}""")

    return titles

def post_article(session, headers, domain: str, json):
    """
    Creates and posts and article for a Ghost article.

    Args:
        session (Session): Verified session instance
        headers (json): Important information for getting requests
        domain (str): Domain of ghost blog
        json (str): Blog post formatted in json
    
    """
    
    # Build url endpoint
    url = f"https://{domain}.ghost.io/ghost/api/admin/posts/?source=html"

    print(f"POSTING TO GHOST:\n\033[32m {json}\033[0m")

    # Publish
    status = session.post(url, headers=headers, json=json)

    # Print diagnostics
    print(f"ATTEMPTED TO POST WITH STATUS: {status}")
