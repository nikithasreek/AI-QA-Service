# 📌 AI QA Service (FastAPI + RAG + LLM)

An AI-powered Question Answering service built using FastAPI, PostgreSQL, Sentence Transformers, and Google Gemini LLM. It implements a Retrieval-Augmented Generation (RAG) pipeline to answer user queries using stored documents. The application is deployed on AWS EC2 with interactive API documentation available through FastAPI Swagger UI.

---

## 🚀 Features

- FastAPI REST API backend
- Sentence Transformer embeddings (`all-MiniLM-L6-v2`)
- PostgreSQL database for document storage
- Cosine similarity-based retrieval system
- Google Gemini LLM integration
- Basic RAG (Retrieval Augmented Generation) pipeline
- Swagger UI for API testing

---

## 🏗️ Project Structure

AI_QA_Service/
│
├── app/
│   ├── main.py          # FastAPI app
│   ├── database.py      # PostgreSQL connection
│   ├── embeddings.py    # Embedding generation
│   ├── retriever.py     # Document retrieval logic
│   └── llm.py           # Gemini LLM integration
│
├── data/
│   └── documents.txt    # Knowledge base
│
├── insert_data.py       # Insert documents into PostgreSQL
├── requirements.txt
├── .env
└── README.md

---

## ⚙️ Installation

### 1. Clone repository
git clone <your-repo-link>
cd AI_QA_Service

---

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

---

### 3. Install dependencies
pip install -r requirements.txt

---

## 🗄️ Database Setup (PostgreSQL)

Run this SQL:

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding FLOAT[]
);

---

## 📥 Insert Data into Database

python insert_data.py

This will:
- Read documents.txt
- Generate embeddings
- Store in PostgreSQL

---

## 🚀 Run the Application

uvicorn app.main:app --reload

---

## 🌐 API Endpoints

### 🔹 Root Endpoint
GET /

Response:
{
  "status": "AI QA service running"
}

---

### 🔹 Ask Question Endpoint
POST /ask

Request:
{
  "question": "What is FastAPI?"
}

Response:
{
  "question": "What is FastAPI?",
  "answer": "FastAPI is a modern Python web framework used to build APIs..."
}

---

## 📚 API Documentation

Once running:

Swagger UI: http://127.0.0.1:8000/docs  
Redoc: http://127.0.0.1:8000/redoc  

---

## 🧠 Architecture

User Question
   ↓
FastAPI Endpoint (/ask)
   ↓
Generate Embedding (Sentence Transformer)
   ↓
Retrieve Similar Documents (PostgreSQL + Cosine Similarity)
   ↓
Send Context to Gemini LLM
   ↓
Generate Final Answer
   ↓
Return Response

---

## ☁️ AWS Deployment (EC2)

Run on server:

uvicorn app.main:app --host 0.0.0.0 --port 8000

Access:

http://<EC2-PUBLIC-IP>:8000/docs


In details:

In Detail: 
## ☁️ AWS EC2 Deployment

The application was deployed on an Ubuntu EC2 instance hosted on AWS.

### 1. Connect to EC2

```bash
ssh -i your-key.pem ubuntu@<EC2-PUBLIC-IP>
```

### 2. Update the server

```bash
sudo apt update && sudo apt upgrade -y
```

### 3. Install required packages

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

### 4. Clone the repository

```bash
git clone https://github.com/nikithasreek/AI-QA-Service.git
cd AI-QA-Service
```

### 5. Create and activate a virtual environment

```bash
python3 -m venv fastapi-env
source ~/fastapi-env/bin/activate
```

### 6. Install dependencies

```bash
pip install -r requirements.txt
pip install sqlalchemy psycopg2-binary
```

### 7. Configure environment variables

Create a `.env` file and add your Google Gemini API key:

```env
GOOGLE_API_KEY2=YOUR_GOOGLE_API_KEY
```

### 8. Run the application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Or run it in the background:

```bash
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
```

### 9. Verify the application

```bash
ps aux | grep uvicorn
```
The API is accessible at:

```
http://<EC2-PUBLIC-IP>:8000
```

Swagger documentation:

```
http://<EC2-PUBLIC-IP>:8000/docs

## 🛠️ Tech Stack

- FastAPI
- Python
- PostgreSQL
- Sentence Transformers
- Google Gemini API
- Uvicorn

---

## 📌 Future Improvements

- FAISS vector database for faster retrieval
- LangChain integration
- Docker containerization
- CI/CD pipeline (GitHub Actions)
- Authentication layer
- Production-grade logging

---

## 👩‍💻 Nikitha Sree K

AI Developer Trainee Assessment Project
