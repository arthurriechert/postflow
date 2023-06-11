from ghost.manager import GhostManager
from llm.openai.model import OpenAIModel

import llm.prompts as prompt
import settings as sg
from parse import parse_json

from dotenv import load_dotenv

def test_openai_vectorize ():
    """
    Test for openai embeddings 

    """
    
    # Initialize OpenAI API
    llm = OpenAIModel()

    print(llm.vectorize(["Hello", "World"]))   

if __name__=="__main__":

    load_dotenv()

    test_openai_vectorize()
