import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from langchain_chroma import Chroma
# (older ver) from langchain.vectorstores import Chroma
from Loaders.PDF_Loader import docs
from Splitters.RecursiveCharacterS import chunks
from chromadb.utils import embedding_functions


# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# chunks = splitter.split_documents(docs)

embedding_function = embedding_functions.DefaultEmbeddingFunction()

vectorstore =Chroma(
    collection_name="my_collection",
    embedding_function=embedding_function,
    persist_directory="vector_db/chroma"
)

vectorstore.add_documents(chunks)

print("Number of chunks added to vectorstore:", len(chunks))
