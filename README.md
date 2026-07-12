
# 📄 AI Document Intelligence

An AI-powered document analysis platform that enables users to summarize documents, chat with PDFs using Retrieval-Augmented Generation (RAG), extract insights, compare documents, and process scanned PDFs using OCR.

---

## 🚀 Features

- 📄 AI-powered document summarization
- 💬 Chat with documents using RAG
- 🔍 Semantic search with FAISS
- 📑 Multi-document support
- 🧾 OCR support for scanned PDFs
- 📝 Meeting Notes mode
- 📌 Keyword extraction
- 📊 Document analytics
- 📥 Download summary as PDF and TXT
- 💾 Export chat history as PDF and Markdown
- 📚 Suggested questions
- 📄 Retrieved source snippets
- 📊 Document comparison with similarity score

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Language:** Python
- **LLM:** Groq (Llama 3.3 70B)
- **Vector Database:** FAISS
- **Embeddings:** Sentence Transformers (MiniLM-L6-v2)
- **OCR:** Tesseract OCR
- **PDF Processing:** pdfplumber, pdf2image
- **Document Processing:** python-docx
- **PDF Generation:** ReportLab

---

## 📂 Project Structure

```text
AI-Document-Intelligence/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── utils/
│   ├── pdf_reader.py
│   ├── rag.py
│   ├── summarizer.py
│   ├── meeting_notes.py
│   ├── keywords.py
│   ├── suggested_questions.py
│   ├── chat_export.py
│   ├── document_compare.py
│   └── ocr_reader.py
│
├── uploads/
├── assets/
└── ...
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/mohapatranirjhala-stack/AI-Document-Intelligence.git
```

### Move into the project

```bash
cd AI-Document-Intelligence
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots inside the `assets/` folder and reference them here.

Example:

```md
![Home](assets/home.png)

![Summary](assets/summary.png)

![Chat](assets/chat.png)

![OCR](assets/ocr.png)

![Comparison](assets/comparison.png)
```

---

## 🎯 Use Cases

- Resume Analysis
- Research Paper Summarization
- Legal Document Analysis
- Meeting Notes Summarization
- Multi-document Question Answering
- OCR for Scanned Documents
- Document Comparison

---

## 🚀 Future Enhancements

- 🌍 AI Translation for multilingual documents
- 📈 Advanced document analytics dashboard
- ☁️ Cloud storage integration
- 👥 User authentication and profiles
- 📑 Batch document processing
- 🤖 Support for multiple LLM providers
- 📊 Interactive visualizations for document insights

---

## 👨‍💻 Author

**Nirjhala Mohapatra**

- 🎓 B.Tech Computer Science Engineering
- 💡 AI | Machine Learning | Full Stack Development
- 🌟 Passionate about building AI-powered applications

GitHub:
https://github.com/mohapatranirjhala-stack

LinkedIn:
(Add your LinkedIn profile link here)

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 💡 Share your feedback
- 🚀 Connect with me on LinkedIn

---

## 🙏 Acknowledgements

This project was built using:

- Streamlit
- Groq LLM (Llama 3.3 70B)
- FAISS
- Sentence Transformers
- Tesseract OCR
- ReportLab
- pdfplumber
- python-docx

---

> Built with ❤️ by **Nirjhala Mohapatra**