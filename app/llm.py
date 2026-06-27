# import os
# from google import genai

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY2")
# )
# def generate_answer(context, question):

#     prompt = f"""
#     Context:
#     {context}

#     Question:
#     {question}
#     """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt
#     )

#     return response.text

# if __name__ == "__main__":

#     context = """
#     FastAPI is a modern Python framework used for building APIs.
#     """

#     question = "What is FastAPI?"

#     answer = generate_answer(context, question)

#     print(answer)

# pip install python-dotenv

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY2")

if not api_key:
    raise ValueError("GOOGLE_API_KEY2 not found in .env file")

client = genai.Client(api_key=api_key)

def generate_answer(context, question):

    prompt = f"""
    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# test

if __name__ == "__main__":
    answer = generate_answer(
        "FastAPI is a Python framework.",
        "What is FastAPI?"
    )

    print(answer)

# import os
# api_key = os.getenv("GOOGLE_API_KEY2")
# print(api_key)