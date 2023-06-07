from ghost.manager import GhostManager
from cli import cli
from llm.openai.model import OpenAIModel

if __name__ == "__main__":
    
    ghost_manager = GhostManager()
    
    openai_model = OpenAIModel() 

    response = openai_model.get_chat_response(message=[{"role": "user", "content": "hello"}])

    print(response)
    
    cli()
