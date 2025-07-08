CONFIG = {
    "verbose": True,    
    "text_splitter": {
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "add_start_index": True
    },
    "embeddings": {
        "model_name": "all-MiniLM-L6-v2",

    },
    # puedes añadir más secciones luego:
    # "llm": {...}
    # "embeddings": {...}
    # "vectorstore": {...}
}