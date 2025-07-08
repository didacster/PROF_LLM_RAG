def compute_coverage(query: str, doc_text: str) -> float:
    query_words = set(query.lower().split())
    doc_words = set(doc_text.lower().split())
    if not query_words:
        return 0.0
    shared = query_words.intersection(doc_words)
    return round(len(shared) / len(query_words), 4)
