def similarity_search(embeddingstore = None, query = None):
    return embeddingstore.similarity_search(query, k=1)
