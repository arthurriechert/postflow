from parse import parse_json, str_to_json, list_to_str, flatten

def get_steps(goal: str, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        goal (str): Goal to accomplish
        model (OpenAIModel): Instance of llm

    Returns:
        steps (str): A list of steps to complete the goal

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are a master planner that creates detailed steps towards completing a goal
                """
            },
        {
            "role": "user",

            "content":

                f"""
                Develop a numbered list of steps to accomplish {goal}
                """
            }
    ]

    # Get a response from the LLM
    steps = model.get_chat_response(message=prompt)

    # Parse output
    steps = parse_json(steps, "content") 

    return steps

def get_post_outline(topic: str, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        topic (str): Blog post topic
        model (OpenAIModel): Instance of model you are using

    Returns:
        outline (str): An outline for a blog post

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are WriterGPT, a genius AI writer that develops cohesive and detailed outlines for blog posts.
                """
            },
        {
            "role": "user",

            "content":

                f"""
                Develop a numbered list of steps to accomplish {goal}
                """
            }
    ]

    # Get a response from the LLM
    outline = model.get_chat_response(message=prompt)

    # Parse response
    outline = parse_json(outline, "content")

    return outline

def get_new_idea(description: str, current: str, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        description (str): Describe purpose or character of your blog
        current (str): List of current articles
        model (OpenAIModel): An instance of OpenAIModel

    Returns:
        article_idea (json): Generates a new idea to use

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are BloggerGPT, and you generate novel ideas for blog post articles. You only reply in json and in no other format.
                Topic must be narrowed and focus to one particular aspect of a subject or a subtopic of a subtopic or a subtopic

                Your response must use the following keys:
                title -> The SEO-friendly title of the article
                slug -> A Descriptive 2-word slug
                description -> A detailed description of what the article is about
                """
            },
        {
            "role": "user",

            "content":

                f"""
                Be very specific and narrow. No broad topics.

                Give me a json based on this description of my blog:
                {description}

                Avoid overlap with this current list of articles:
                {current}
                """
            }
    ]

    # Get a response from the LLM
    idea = model.get_chat_response(message=prompt)

    # Parse output
    idea = parse_json(idea, "content") 

    # Flatten list
    idea = flatten(idea)

    # Convert a list to a string
    idea = list_to_str(idea)

    # Convert to json
    idea = str_to_json(idea)

    return idea


def format_blog_post(outline: list, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        outline (str): Outline of the article
        model (OpenAIModel): An instance of OpenAIModel

    Returns:
        article_idea (json): Generates a new idea to use

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are FormatterGPT, and you generate a comprehensive, engaging, and SEO-friendly articles in Ghost. You only reply in json and in no other format.

                Follow this example response exactly, do not include any boilerplate, only put your response in this format:

                
                {
                    "version": "5.1",
                    "atoms": [],
                    "cards": [],
                    "markups": [["strong"], ["em"], ["a", ["href", "https://www.example.com"]]],
                    "sections": [
                        [1, "h2", [
                            [0, [], 0, "Heading"]
                        ]],
                        [1, "p", [
                            [0, [], 0, "This is a paragraph with "],
                            [0, [0], 1, "bold"],
                            [0, [], 0, " and "],
                            [0, [1], 1, "italic"],
                            [0, [], 0, " text."]
                        ]],
                        [3, "ul", [
                            [[0, [], 0, "List item 1"]],
                            [[0, [], 0, "List item 2"]]
                        ]],
                        [1, "blockquote", [
                            [0, [], 0, "This is a quote."]
                        ]],
                        [1, "p", [
                            [0, [], 0, "This is a link to "],
                            [0, [2], 1, "example.com"],
                            [0, [], 0, "."]
                        ]]
                    ]
                }       

                """
            },
        {
            "role": "user",

            "content":

                f"""
                Give me a json based on this article draft of my blog post and must use every part of the draft.
                {outline}
                """
            }
    ]

    # Get a response from the LLM
    article = model.get_chat_response(message=prompt)

    # Parse output
    article = parse_json(article, "content") 

    # Flatten list
    article = flatten(article)

    # Convert a list to a string
    article = list_to_str(article)

    # Convert to json
    article = str_to_json(article)

    return article


def get_outline(details: str, model):
    """
    Prompt to generate an outline for an article

    Args:
        details (str): Receives title and description in json-formatted string
        model (OpenAIModel): An instance of OpenAIModel

    Returns:
        outline (str): A string of html outline

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are BloggerGPT, and you generate an outline for given bog posts. You only reply in json and in no other format.

                Your response must consider these rules:
                1) Comprehensive
                2) Cohesive
                3) Organized for SEO
                4) Makes use of subheadings
                5) Only in json
                """
            },
        {
            "role": "user",

            "content":

                f"""
                Be very specific and narrow. No broad topics.

                Here are the details for the post:
                {details}
                """
            }
    ]

    # Get a response from the LLM
    outline = model.get_chat_response(message=prompt)

    # Parse output
    outline = parse_json(outline, "content") 

    # Flatten list
    outline = flatten(outline)

    # Convert a list to a string
    outline = list_to_str(outline)

    # Convert to json
    outline = str_to_json(outline)

    return outline

def write_blog_post(outline: list, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        outline (str): Outline of the article
        model (OpenAIModel): An instance of OpenAIModel

    Returns:
        article_idea (json): Generates a new idea to use

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "role": "system",

            "content":

                """
                You are BloggerGPT, and you generate a comprehensive, engaging, and SEO-friendly articles in Ghost. Make sure to distinguish between lists, headings, and subheadingsl
                """
            },
        {
            "role": "user",

            "content":

                f"""
                Give me a fully-written article based on this article outline of my blog post and must use every part of the outline.
                {outline}
                """
            }
    ]

    print(f"\nSENDING: {prompt}")

    # Get a response from the LLM
    article = model.get_chat_response(message=prompt)

    # Parse output
    article = parse_json(article, "content") 

    # Flatten list
    article = flatten(article)

    # Convert a list to a string
    article = list_to_str(article)

    return article



