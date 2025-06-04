import streamlit as st
from pdf_reader import extract_text_from_pdf
from gemini_chat import ask_gemini_about_pdf

# Set page config
st.set_page_config(page_title="OncoOral AI Chatbot with Gemini", layout="centered")

# App title
st.image("C:/Users/Siyumi Jayawardhane\OneDrive - Informatics Institute of Technology/Certificates/Oral_Cancer_Risk_Presdiction_Chatbot/oncoral.png", width=100)
st.title("OncoOral AI - Chatbot")
st.markdown("Ask questions about Oral cancer")

# PDF path
PDF_PATH = "C:/Users/Siyumi Jayawardhane/OneDrive - Informatics Institute of Technology/Certificates/Oral_Cancer_Risk_Presdiction_Chatbot/OralCancer.pdf"

# Load PDF content once and cache it
@st.cache_data
def load_pdf_text():
    return extract_text_from_pdf(PDF_PATH)

pdf_text = load_pdf_text()

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form("chat_form", clear_on_submit=True):
    user_question = st.text_input("Ask a question about Oral cancer:")
    submitted = st.form_submit_button("Ask")

if submitted and user_question:
    # Get answer from Gemini
    answer = ask_gemini_about_pdf(pdf_text, user_question)
    
    # Store and display chat history
    st.session_state.chat_history.append(("You", user_question))
    st.session_state.chat_history.append(("Gemini", answer))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Gemini:** {msg}")
