# from app.embeddings import generate_embedding

# text = "FastAPI is a modern Python framework"
# embedding = generate_embedding(text)
# print(len(embedding))

from app.database import SessionLocal
from app.embeddings import generate_embedding
from sqlalchemy import text

# read file
with open("data/documents.txt", "r", encoding="utf-8") as f:
    docs = f.readlines()

db = SessionLocal()

for doc in docs:
    emb = generate_embedding(doc.strip())

    db.execute(
        text("INSERT INTO documents (content, embedding) VALUES (:content, :embedding)"),
        {"content": doc.strip(), "embedding": emb}
    )

db.commit()
db.close()

print("✅ Data inserted successfully")