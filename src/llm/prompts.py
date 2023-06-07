def get_steps(goal: str, model):
    """
    Prompt to generate a list of steps to complete the goal

    Args:
        goal (str): Goal to accomplish

    Returns:
        steps (str): A list of steps to complete the goal

    """

    # Format prompt as a list of dictionaries
    prompt = [
        {
            "system":

                """
                You are a master planner that creates detailed steps towards completing a goal
                """
            }
        {
            "user":

                f"""
                Develop a numbered list of steps to accomplish {goal}
                """
            }
    ]

    # Get a response from the LLM
    steps = model.get_chat_response(message=prompt)

    return steps
