import json

import os

import db.vector.load as vector

def create_default_toolkit():
    """
    Creates a default toolkit if one doesn't already exist

    Args:
        None

    Returns:
        None

    """

    toolkit = {
        "Google Search": "Google Search, also known simply as Google, is a web search engine developed by Google LLC. It is the most widely used search engine across the globe, and its main purpose is to search for text in publicly accessible documents offered by web servers. Google Search provides numerous options for customized search, using symbols or operators in the search box to filter and refine the search results. Google Search can handle queries containing text, numbers, and special characters. It provides results for a variety of content, including websites, images, videos, news, and maps. Common uses include finding specific information, researching topics, locating online resources, and navigating the web."
    }

    with open("tools/toolkit.json", 'w') as file:
        json.dump(toolkit, file)

        
