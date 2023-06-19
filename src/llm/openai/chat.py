from llm.openai.model import OpenAIModel
import time
import json
import os
from typing import Optional
from parse import parse_json, flatten

def start_history(system_seed: str, user_seed: str, path: str = "./llm/openai/chat_history.json") -> Optional[int]:
    if os.path.exists(path):
        return None
    
    print(f"\n\033[33mCreating a new chat history at {path}\033[0m")
    with open(path, 'w') as file:
        json.dump([{"role": "system", "content": system_seed},{"role": "user", "content": user_seed}], file)

    print(f"\n\033[32mCreated a new chat history at {path}\033[0m") 

    return 1


def destroy_history(path: str = "./llm/openai/chat_history.json") -> None:
    if os.path.exists(path):
        os.remove(path)
        print(f"\n\033[32mSuccessfully removed chat history at {path}\033[0m")
        return None

    print(f"\n\033[33mNo chat history exists at {path}\033[0m")
    return None

def read_history(path: str = "./llm/openai/chat_history.json") -> Optional[list]:
    if not os.path.exists(path):
        print(f"\n\033[31mNo chat history at {path}\033[0m")
        return None

    with open(path, 'r') as file:
        return json.load(file)

def append_history(messages: list, path: str = "./llm/openai/chat_history.json") -> None:
    chat_history: list = read_history()
    if not chat_history:
        print(f"\n\033[31mFailed to read the chat history at {path}\033[0m")
        return None

    chat_history.extend(messages)

    with open(path, 'w') as file:
        json.dump(chat_history, file)
        return None

def chat(new_message: str, role: str = "user") -> Optional[str]:
    
    llm = OpenAIModel()

    if not start_history(system_seed="You are an assistant and will answer any questions asked of you", user_seed=new_message):
        append_history([{"role": role, "content": new_message}])

    history = read_history() 

    response = llm.get_chat_response(history)

    assistant_response = flatten(parse_json(response, "content"))[0]

    append_history([{"role": "assistant", "content": assistant_response}])

    return assistant_response
