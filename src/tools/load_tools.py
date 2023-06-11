import json

import os

import db.vector.load as vector

from parse import parse_json

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
    vector.save_to_db(tool_vectors, "db/vector/tools")

    print(f"\nSuccessfully stored tools")


