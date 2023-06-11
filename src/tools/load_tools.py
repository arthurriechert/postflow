import json

import os

import db.vector.load as vector

from parse import parse_json, flatten

def create_default_toolkit():
    """
    Creates a default toolkit if one doesn't already exist

    Args:
        None

    Returns:
        None

    """

    toolkit = {
        
       "Google Search": {
                
            "description": "Google Search, also known simply as Google, is a web search engine developed by Google LLC. It is the most widely used search engine across the globe, and its main purpose is to search for text in publicly accessible documents offered by web servers. Google Search provides numerous options for customized search, using symbols or operators in the search box to filter and refine the search results. Google Search can handle queries containing text, numbers, and special characters. It provides results for a variety of content, including websites, images, videos, news, and maps. Common uses include finding specific information, researching topics, locating online resources, and navigating the web.",
                
            "index": 0
        },

       "Python Interpreter": {
            
           "description": "A Python interpreter is a software tool that executes code written in the Python programming language. It takes Python code as input, parses it to convert into intermediate byte-code, and then translates this byte-code into the native language of your computer. Python is an interpreted language, meaning that it doesn't need to be compiled before it's run, unlike languages such as C or Java. This Python interpreter is an integral part of any Python development environment, enabling developers to write and execute Python code. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Additionally, the Python interpreter can be used in an interactive mode, where lines of code can be written and executed one at a time, making it a valuable tool for quick prototyping and testing of code snippets. It is widely used for a variety of software development tasks, including web development, data analysis, artificial intelligence, machine learning, automation, and more.",

           "index": 1
       }
    }

    with open("tools/toolkit.json", 'w') as file:
        json.dump(toolkit, file)


def load_toolkit():
    """
    Loads toolkit from a file.

    Args:
        None

    Returns:
        Tools (list): A list of tools

    """

    # Create default toolkit if it doesn't exist
    if not os.path.exists("tools/toolkit.json"):

        print(f"\nThe path, tools/toolkit.json, does not exist. Creating default toolkit")

        create_default_toolkit()

    with open("tools/toolkit.json", 'r') as file:
        tools = json.load(file)

    return tools

def load_tool(tool_name: str):
    """
    Loads a specific tool from a file

    Args:
        tool_name (str): The specific toolname key from the file

    Returns:
       tool (str): The dictionary containing index and description of tool 

    """
    
    # Get tools
    tools = load_toolkit()

    # Parse tools
    tool = parse_json(tools, tool_name)

    # Check if you found anything
    if not tool:
        print(f"{tool_name} is not an available tool")

    return tool

def vectorize_tools(toolkit: dict, llm):
    """
    Stores tool JSON in a FAISS index

    Args:
        toolkit (dict): A json containing our tools
        llm: An instance storing an LLM

    Returns:
        None

    """

    descriptions = []

    # Iterate over toolkit
    for tool, characteristic in toolkit.items():

        # Assemble list to vectorize
        descriptions.append(characteristic["description"])

    # Get embedings
    tool_vectors = llm.vectorize(descriptions)

    # Store file index
    vector.save_to_db(tool_vectors, "db/vector/indices/tools")

    print(f"\nSuccessfully stored tools")

def find_tool(query: str, llm):
    """
    Locates a tool that ChatGPT wants to use

    Args:
        query (str): A question to message from AI
        llm: An instance of an AI model

    Returns:
        tools (list): A list of closely related tools

    """

    query = "Search the Internet"

    # Do a search
    tool_indices = vector.query_db(query, llm, 1, "db/vector/indices/tools")

    # Convert to a list
    tool_indices = flatten(tool_indices.tolist())

    # Get our reference
    tool_list = load_toolkit()

    # Placeholder
    tools = []

    # Iterate over toollist
    for tool, characteristic in tool_list.items():
        
        # Search for relevant tools
        for index in tool_indices:
            
            if characteristic["index"] == index:
                tools.append(tool)
    
    return tools

