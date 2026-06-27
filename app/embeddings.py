from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def generate_embedding(text):
    return model.encode(text).tolist()
# # Test
# embedding = generate_embedding(
#     "FastAPI is a modern Python framework."
# )

# print("Embedding length:", len(embedding))
# print(embedding[:5])