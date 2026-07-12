
import streamlit as st
from utils.pdf_reader import extract_text
from utils.summarizer import generate_summary
from utils.rag import create_vector_store, ask_question
from utils.pdf_generator import generate_pdf
from utils.suggested_questions import get_suggested_questions
from utils.keywords import extract_keywords
from utils.meeting_notes import generate_meeting_notes
from utils.document_compare import compare_documents
from utils.multi_document import extract_multiple_documents
from utils.chat_export import (
    export_chat_pdf,
    export_chat_markdown
)

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# Session State
# -----------------------------------
if "summary" not in st.session_state:
    st.session_state.summary = ""

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

# -----------------------------------
# Title
# -----------------------------------
st.title("📄 AI Document Intelligence")

st.caption(
    "Summarize documents • Chat with your files • Semantic Search using AI"
)

st.markdown("---")

st.info(
"""
### 🚀 AI Powered Document Understanding

Upload PDF, DOCX or TXT documents.

✅ AI Summary

✅ Ask Questions

✅ Semantic Search (FAISS)

✅ Powered by Groq Llama 3.3 70B
"""
)

st.divider()

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("⚙️ AI Settings")

summary_length = st.sidebar.selectbox(
    "Summary Length",
    ["Short", "Medium", "Long"]
)

document_type = st.sidebar.selectbox(
    "📄 Document Type",
    [
        "General Document",
        "Resume",
        "Research Paper",
        "Meeting Notes"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("🤖 Model")

st.sidebar.write("Llama 3.3 70B")

st.sidebar.info(
"""
Vector Database

FAISS

Embedding Model

MiniLM-L6-v2
"""
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Supported Files

• PDF
• DOCX
• TXT
"""
)

# -----------------------------------
# Upload Section
# -----------------------------------
st.subheader("📂 Upload Document")

uploaded_files = st.file_uploader(
    "Choose one or more documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# -----------------------------------
# After Upload
# -----------------------------------
if uploaded_files:

    st.success(
        f"✅ {len(uploaded_files)} document(s) uploaded successfully!"
    )

    total_size = sum(
        file.size for file in uploaded_files
    ) / 1024

    st.info(
        f"""
📄 Documents: {len(uploaded_files)}

📦 Total Size: {total_size:.2f} KB
"""
    )

    document_text = extract_multiple_documents(
        uploaded_files
    )

    st.session_state.document_text = document_text

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document Content",
        document_text,
        height=300
    )

    with st.spinner("Creating Vector Database..."):

        st.session_state.vector_store = create_vector_store(
            document_text
        )

    if st.button("🚀 Generate Summary"):

        with st.spinner("Generating AI Summary..."):

            if document_type == "Meeting Notes":

                st.session_state.summary = generate_meeting_notes(
                    document_text
                )

            else:

                st.session_state.summary = generate_summary(
                    document_text,
                    summary_length
                )

        st.rerun()
# ===================================
# 📑 Document Comparison Section
# ===================================

st.markdown("---")

st.subheader("📑 Compare Two Documents")

compare_files = st.file_uploader(
    "Upload exactly two documents",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
    key="compare_docs"
)
if compare_files:

    if len(compare_files) != 2:

        st.warning(
            "⚠️ Please upload exactly TWO documents."
        )

    else:

        text1 = extract_text(
            compare_files[0]
        )

        text2 = extract_text(
            compare_files[1]
        )

        comparison = compare_documents(
            text1,
            text2
        )

        st.success(
            "✅ Comparison Completed"
        )

        st.metric(
            "Similarity",
            f"{comparison['similarity']}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("➕ Added Content")

            if comparison["added"]:

                for line in comparison["added"][:20]:

                    if line.strip():

                        st.write("•", line)

            else:

                st.info("No added content.")

        with col2:

            st.subheader("➖ Removed Content")

            if comparison["removed"]:

                for line in comparison["removed"][:20]:

                    if line.strip():

                        st.write("•", line)

            else:

                st.info("No removed content.")
# -----------------------------------
# Summary Section
# -----------------------------------
if st.session_state.summary != "":

    st.success("✅ Summary Generated Successfully!")

    st.subheader("📝 AI Generated Summary")

    st.code(
        st.session_state.summary,
        language="text"
    )

    st.divider()

    st.subheader("📊 Document Analytics")

    words = len(
        st.session_state.document_text.split()
    )

    characters = len(
        st.session_state.document_text
    )

    reading_time = max(1, words // 200)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📝 Words",
            words
        )

    with col2:
        st.metric(
            "🔤 Characters",
            characters
        )

    with col3:
        st.metric(
            "⏱ Reading Time",
            f"{reading_time} min"
        )

    st.divider()

    st.subheader("📥 Download Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="📄 Download Summary (.txt)",
            data=st.session_state.summary,
            file_name="summary.txt",
            mime="text/plain"
        )

    with col2:

        pdf_file = generate_pdf(
            st.session_state.summary
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📕 Download Summary (.pdf)",
                data=pdf,
                file_name="summary.pdf",
                mime="application/pdf"
            )

    st.divider()

    st.subheader("📌 Top Keywords")

    keywords = extract_keywords(
        st.session_state.document_text
    )

    cols = st.columns(2)

    for index, (word, count) in enumerate(keywords):

        with cols[index % 2]:

            st.metric(
                label=word.title(),
                value=count
            )

    st.divider()
# -----------------------------------
# Chat Section
# -----------------------------------
if st.session_state.vector_store is not None:

    st.subheader("💬 Chat with your Document")

    st.markdown("### 💡 Suggested Questions")

    questions = get_suggested_questions()

    cols = st.columns(2)

    for index, question_text in enumerate(questions):

        with cols[index % 2]:

            if st.button(
                question_text,
                key=f"suggestion_{index}"
            ):

                with st.spinner("Thinking..."):

                    answer, docs = ask_question(
                        st.session_state.vector_store,
                        question_text
                    )

                source_snippets = []

                for doc in docs:
                    source_snippets.append(
                        doc.page_content[:300]
                    )

                st.session_state.chat_history.append(
                    (
                        question_text,
                        answer,
                        source_snippets
                    )
                )

                st.rerun()

    st.markdown("---")

    question = st.text_input(
        "Ask anything about this document"
    )

    col1, col2 = st.columns(2)

    with col1:

        ask_button = st.button("🤖 Ask AI")

    with col2:

        clear_button = st.button("🗑️ Clear Chat")

    if clear_button:

        st.session_state.chat_history = []

        st.rerun()

    if ask_button:

        if question.strip() == "":

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner("Thinking..."):

                answer, docs = ask_question(
                    st.session_state.vector_store,
                    question
                )

            source_snippets = []

            for doc in docs:

                source_snippets.append(
                    doc.page_content[:300]
                )

            st.session_state.chat_history.append(
                (
                    question,
                    answer,
                    source_snippets
                )
            )

            st.rerun()

# -----------------------------------
# Conversation
# -----------------------------------
if len(st.session_state.chat_history) > 0:

    st.markdown("---")

    st.subheader("📝 Conversation")
    st.markdown("### 📥 Export Chat History")

    pdf_path = export_chat_pdf(
        st.session_state.chat_history
    )

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📄 Download Chat (PDF)",
            data=pdf_file,
            file_name="chat_history.pdf",
            mime="application/pdf"
        )

    markdown_data = export_chat_markdown(
        st.session_state.chat_history
    )

    st.download_button(
        label="📝 Download Chat (Markdown)",
        data=markdown_data,
        file_name="chat_history.md",
        mime="text/markdown"
    )

    st.markdown("---")

    for q, a, snippets in st.session_state.chat_history:

        st.markdown("### 🙋 You")

        st.info(q)

        st.markdown("### 🤖 AI")

        st.success(a)

        with st.expander(
            "📄 Retrieved Source Snippets"
        ):

            for i, snippet in enumerate(
                snippets,
                start=1
            ):

                st.markdown(
                    f"**Snippet {i}**"
                )

                st.write(snippet)

                st.markdown("---")

    for q, a, snippets in st.session_state.chat_history:

        st.markdown("### 🙋 You")

        st.info(q)

        st.markdown("### 🤖 AI")

        st.success(a)

        with st.expander(
            "📄 Retrieved Source Snippets"
        ):

            for i, snippet in enumerate(
                snippets,
                start=1
            ):

                st.markdown(
                    f"**Snippet {i}**"
                )

                st.write(snippet)

                st.markdown("---")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.caption(
    "🚀 Built with Python • Streamlit • FAISS • Sentence Transformers • Groq LLM"
)