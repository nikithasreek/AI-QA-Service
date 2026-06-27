# import numpy as np
# def cosine_similarity(a,b):
#     return np.dot(a,b) / (
#         np.linalg.norm(a)
#         *
#         np.linalg.norm(b)
#     )

# import numpy as np

# def retrieve_document(question):
#     return "FastAPI is a modern Python framework used for building APIs."

# if __name__ == "__main__":
#     result = retrieve_document("What is FastAPI?")
#     print(result)

from app.database import SessionLocal
from sqlalchemy import text
from app.embeddings import generate_embedding
import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_document(question, top_k=2):
    db = SessionLocal()

    question_embedding = generate_embedding(question)

    result = db.execute(text("SELECT content, embedding FROM documents"))
    rows = result.fetchall()

    scored_docs = []

    for content, embedding in rows:
        score = cosine_similarity(question_embedding, embedding)
        scored_docs.append((content, score))

    db.close()

    # sort by similarity
    scored_docs.sort(key=lambda x: x[1], reverse=True)

    top_docs = [doc[0] for doc in scored_docs[:top_k]]

    return "\n".join(top_docs)