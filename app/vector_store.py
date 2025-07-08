def embeddings(verbose=True, all_splits=None):

    """
    Creation of embeddings from a list of text chunks.

    Args:
        all_splits (List[Document]): Lista de fragmentos de texto (chunks), normalmente generados con un splitter.
        verbose (bool): Si True, muestra mensajes del proceso.

    Returns:
        FAISS: Objeto FAISS que contiene los embeddings indexados para búsqueda semántica.
    """

    from langchain_community.vectorstores import FAISS
    from config.config import CONFIG
    from langchain_huggingface import HuggingFaceEmbeddings
    import os

    if verbose:
        print(f"Creating embeddings with model: {CONFIG['embeddings']['model_name']}")

    enbeddingstore_path = "../data/enbeddingstore"
    embeddings = HuggingFaceEmbeddings(model_name=CONFIG["embeddings"]["model_name"])

    enbeddingstore = FAISS.from_documents(all_splits, embeddings)

    #save the vectorstore to disk or load it if it already exists
    if os.path.exists(os.path.join(enbeddingstore_path, "index.faiss")) and os.path.exists(os.path.join(enbeddingstore_path, "index.pkl")):
        if verbose:
            print("Loading existing FAISS index...")
        embeddingstore = FAISS.load_local(enbeddingstore_path, 
                                        embeddings, 
                                        allow_dangerous_deserialization=True)
    else:
        if verbose:
            print("Creating new FAISS index from documents...")
        embeddingstore = FAISS.from_documents(all_splits, embeddings)
        os.makedirs(enbeddingstore_path, exist_ok=True)
        embeddingstore.save_local(enbeddingstore_path)

    return embeddingstore