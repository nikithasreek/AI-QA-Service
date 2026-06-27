from fastapi import FastAPI
from pydantic import BaseModel

from app.retriever import retrieve_document
from app.llm import generate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI QA service running"}

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(data: Question):
    try:
        context = retrieve_document(data.question)

        if not context:
            context = "No relevant context found."

        answer = generate_answer(context, data.question)

        return {
            "question": data.question,
            "context": context,
            "answer": answer
        }

    except Exception as e:
        return {
            "error": str(e)
        }




# from fastapi import FastAPI
# from pydantic import BaseModel
# from app.llm import generate_answer

# app = FastAPI()

# class Question(BaseModel):
#     question: str

# @app.post("/ask")
# def ask(data: Question):

#     context = """
#     FastAPI is a modern Python framework used for building APIs.
#     """

#     answer = generate_answer(
#         context,
#         data.question
#     )

#     return {
#         "question": data.question,
#         "answer": answer
#     }

# uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs