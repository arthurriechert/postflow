def get_post(slug: str, session, headers):
    """
    Obtains content from a ghost page
    
    Args:
        session (Session): Verified session instance
        slug (str): Page name
        headers (json): Important information for getting requests

    Returns:
        data (json): Data from the page

    """

    # Build URL with slug
    url = f"https://cybrco.ghost.io/ghost/api/admin/posts/slug/{slug}"

    # Get the post
    post = session.get(url, headers=headers)

    # Print post
    print(f"""
    ########## RETRIEVED POST  ##########

    STATUS CODE: {post.status_code}

    {post.json()}""")
