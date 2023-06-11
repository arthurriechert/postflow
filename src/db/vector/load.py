# Manage vector db
import faiss

# Manipulating vectors
import numpy as np

# Checking files
import os

# Logging changes
import json

def create_new_db(vectors, path:str):
    """
    Creates a new faiss index

    Args:
        vector (list): A list of vectors to add to an index
        path (str): The path for storing the index

    Returns:
        None

    """

    # Convert to 2-D np array
    vectors = np.vstack(vectors)

    # Measure number of features
    features = vectors.shape[1]

    # Initialize FAISS index
    index = faiss.IndexFlatL2(features)

    # Add the vectors
    index.add(vectors)

    # Store in a file
    faiss.write_index(index, path)

    # Print diagnostics
    print(f"\nCreated new FAISS index at path: {path} and with {index.ntotal} entries.")

def db_exists(path: str):
    """
    Checks if a database exists
    
    Args:
        path (str): File path to the FAISS index

    Returns:
        (bool): If there is a index

    """

    # Look for the path
    if os.path.exists(path):
        return True
    else:
        return False


def load_db(path: str):
    """
    Loads a FAISS index from file

    Args:
        path (str): The path for a storing an index

    Returns:
        index: FAISS index
        exists (bool): True when index exists

    """

    # Determine if the path exists
    if (db_exists(path)):

        # Read file
        index = faiss.read_index(path)
        
        # Print diagnostics
        print("\n\033[32mIndex located and loads\033[0m")

        return index, True

    else:

        return "Argggh! You flubbed up", False
        

def save_to_db(vectors, path: str):
    """
    Saves vectors to a FAISS index file

    Args:
        vectors (list): A list of embeddings received from ChatGPT
        path (str): Location of the index

    Returns:
        None 

    """
    
    # Attempt to locate exists db
    index, exists = load_db(path)

    # Create new index file
    if exists:
        index.add(np.array(vectors))
        faiss.write_index(index, path)
        print(f"\nSuccessfully saved vectors to: {path}")
    else:
        create_new_db(vectors, path)
        print(f"\nFailed to find index. Created new vector database at {path}")


def query_db(query: str, llm, k: int, path: str):
    """
    Perform an L2 similarity search over FAISS index

    Args:
        query (str): A question to encode and ask the db
        llm: An AI model to encode the query
        k (int): The number of neighbors to return
        path (str): Path where the db is located

    Return:
        indices (ndarray): Np array containing indices for nearest neighbors

    """

    # Get embedding
    embedding = np.array(llm.vectorize(query)).reshape(1, -1)

    # Load db
    index,_ = load_db(path)

    # Do search
    _,indices = index.search(embedding, k)

    return indices
