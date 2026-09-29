from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

if __name__ == "__main__":
    text = "The Transformer is based on attention mechanisms."
    vector = embeddings.embed_query(text)
    print("Vector length:", len(vector))
    print(vector[:5])