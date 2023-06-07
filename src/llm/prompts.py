from parse import parse_json

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
                Give me a json based on this description of my blog:
                {description)

                Avoid overlap with this current list of articles:
                {current}
                """
            }
    ]

    # Get a response from the LLM
    idea = model.get_chat_response(message=prompt)

    # Parse output
    idea = parse_json(idea, "content") 

    # Convert to json

    return idea


