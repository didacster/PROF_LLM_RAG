CONFIG = {
    "verbose": True,    
    "text_splitter": {
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "add_start_index": True
    },
    "embeddings": {
        "model_name": "thenlper/gte-small",

    },
    # puedes añadir más secciones luego:
    # "llm": {...}
    # "embeddings": {...}
    # "vectorstore": {...}
}