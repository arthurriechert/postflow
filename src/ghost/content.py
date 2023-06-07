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

def parse_json(json, keys):
    """
    Returns a list containing based on desired keys

    Args:
        key (list or str): Contains desired keys used to find json information
        json (json): Contains data to parse

    Returns:
        results (list): Contains associated values from key

    """

    # Initialize placeholder list
    results = []

    # Recursively iterate over json elements
    if isinstance(json, dict):
        for key, value in json.items():
            if key == keys:
                results.append(value)
            else:
                values = parse_json(value, keys)
                if values: results.append(values)
    elif isinstance(json, list):
        for item in json:
            values = parse_json(item, keys)
            if values: results.append(values)

    return results

def flatten(nested_list):
    """
    Convert a nested list to flat list

    Args:
        nested_list (list): A list containing lists
    
    Returns:
        flattened_list (list): A list not containing lists

    """

    # Initialize placeholder variable
    flattened_list = []

    # Recursively remove dimensions
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)

    return flattened_list

def remove_duplicate_elements(input_list: list):
    """
    Removes duplicate elements from a list by converting it to a set and back

    Args:
        input_list (list): A list contain duplicates

    Returns:
        output_list (list): A list without duplicates

    """

    # Convert list to set and back to list
    output_list = list(set(input_list))

    return output_list

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

def get_slugs(session, headers, domain: str):
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
