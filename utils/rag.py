
import os
from dotenv import load_dotenv
from groq import Groq

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_vector_store(document_text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(document_text)

    vector_store = FAISS.from_texts(
        chunks,
        embedding_model
    )

    return vector_store


def ask_question(vector_store, question):

    docs = vector_store.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer ONLY using the context below.

If the answer is not present, reply:

'I couldn't find that information in the uploaded document.'

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    answer = response.choices[0].message.content

    return answer, docs