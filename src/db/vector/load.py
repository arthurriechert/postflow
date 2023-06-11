# Manage vector db
import faiss

# Manipulating vectors
import numpy as np

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
    features = np.shape[1]

    # Initialize FAISS index
    index = faise.IndexFlatL2(features)

    # Add the vectors
    index.add(vectors)

    # Store in a file
    faiss.write_index(index, path)

    # Print diagnostics
    print(f"\nCreated new FAISS index at path: {path} and with {index.ntotal} entries.")
