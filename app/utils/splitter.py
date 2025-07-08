
def split_text(text, chunk_size=1000, chunk_overlap=200, add_start_index=True):
    """
    Splits the input text into smaller chunks based on the specified parameters.
    
    Args:
        text (str): The text to be split.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.
        add_start_index (bool): Whether to add a start index to each chunk.
        
    Returns:
        list: A list of text chunks.
    """
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=add_start_index
    )
    
    return splitter.split_documents(text)