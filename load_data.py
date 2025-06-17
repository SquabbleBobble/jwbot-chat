import pickle

def load_vectorstore():
    with open("vector_store.pkl", "rb") as f:
        return pickle.load(f)# Loads pre-chunked jw.org data
