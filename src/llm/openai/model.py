import openai

class Model:
    """
    Creates a class that will get completions or response from ChatGPT

    """

    def __init__(self):
    """
    Constructor to create an instance of Model

    Vars:
        chat_model (str): Chat model for the api
        completion_model (str): Completion model for the api
        embedding_model (str): Gets embeddings from api
        temperature (float): Determines predictability of output
        max_tokens (int): Max input size
