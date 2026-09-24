from langchain_text_splitters import CharacterTextSplitter
from Loaders import PDF_Loader


splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(PDF_Loader.docs)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)
    print("Length:", len(chunk.page_content))