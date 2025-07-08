import os

from retriever import similarity_search
from config.config import CONFIG
from utils.splitter import split_text
from vector_store import embeddings
from langchain_community.document_loaders import PyPDFLoader

def main():
  verbose = CONFIG["verbose"]

  # Define the folder where the PDFs are located
  current_dir = os.path.dirname(os.path.abspath(__file__))
  folder_path = os.path.abspath(os.path.join(current_dir, "..", "data"))
  pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]

  docs = []

  # Check for available PDFs
  if not pdf_files:
      print("No PDF files found in the folder.")
  else:
      for pdf_file in pdf_files:
          pdf_path = os.path.join(folder_path, pdf_file)

          if verbose:
              print(f"\nReading the file: {pdf_file}")

          loader = PyPDFLoader(pdf_path)
          documents = loader.load()

          docs.extend(documents)

  # Split the documents into smaller chunks
  all_splits = split_text(
    docs,
    chunk_size=CONFIG["text_splitter"]["chunk_size"],
    chunk_overlap=CONFIG["text_splitter"]["chunk_overlap"],
    add_start_index=CONFIG["text_splitter"]["add_start_index"]
  )

  if verbose:
    print(f"we have divided the text into {len(all_splits)} parts with an overlap of {CONFIG["text_splitter"]["chunk_overlap"]} words.")

  #create embeddings
  embeddingstore = embeddings(verbose=verbose, all_splits=all_splits)

  query = input("Enter your question: ")

  # Similarity search
  docs_retrieved = similarity_search(embeddingstore = embeddingstore, query = query)

if __name__ == "__main__":
    main()