import openai

import os
import json

from dotenv import load_dotenv

from parse import parse_json

class OpenAIModel:
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

        """

        # Set the model versions
        self.chat_model = os.getenv("OPENAI_CHAT_MODEL")
        self.completion_model = os.getenv("OPENAI_COMPLETION_MODEL")
        self.embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL")
        
        # Load the settings.json
        with open("settings.json", "r") as file:
            self.settings = json.load(file)
        
        # Iterate over settings
        for key, value in self.settings.items():
            self.temperature = value if key == "temperature" else 0.5
            self.max_tokens = value if key == "max_tokens" else 2048

        self.llm = openai
        self.llm.api_key = os.getenv("OPENAI_API_KEY")

    def get_chat_response(self, message: list):
        """
        Sends chat to LLM

        Args:
            message (list): Chat history formatted as a list dictionaries

        Returns:
            response (str): Response from the LLM

        """
        
        # Format request and send
        response = self.llm.ChatCompletion.create(
            model = self.chat_model,
            messages = message,
            temperature = self.temperature,
            max_tokens = self.max_tokens
        )

        # Parse reponse
        # response = parse_json(response, "content")#response["choices"][0]["message"]["content"]

        return response

    def get_completion_response(self, message: str):
        """
        Sends completion request to LLM

        Args:
            message (str): String to complete

        Returns:
            response (str): String to get completion for

        """

        # Format request and send
        reponse = self.llm.Completion.create(
            model = self.completion_model,
            prompt = message,
            temperature = self.temperature,
            max_tokens = self.max_tokens
        )

        # Parse reponse
        response = response.choices[0].text.strip()

        return response

    def vectorize(self, text):
        """
        Sends a string to OpenAI embedding model and returns a vector

        Args:
            text (str or list): String to vectorize
            json_parser (function): A function that can parse json

        Returns:
            vectors (list): Vector returned by embeding model

        """

        # Check if we are sending a list or string
        if isinstance(text, str):
            
            # Print diagnostic
            print(f"\nVectorizing: {text}")

            # Get embedding
            embedding = self.llm.Embedding.create(
                input=text,
                model=self.embedding_model
            )

            # Parse JSON
            vectors = embedding["data"][0]["embedding"]

            return vectors
            
        elif isinstance(text, list):

            # Print diagnostic
            print(f"\nVectorizing: {[i for i in text]}")

            vectors = []

            # Recursively iterate over to get individual embeddings
            for string in text:

                vectors.append(self.vectorize(string))

            print(f"Retrieved list of {len(vectors)} embeddings")

            return vectors
