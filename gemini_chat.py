import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini_about_pdf(pdf_text, question):
    prompt = f"""You are a helpful assistant. Answer the following question based on this PDF content:

    PDF Content:
    {pdf_text[:10000]}  # Limit to 10k chars

    Question: {question}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
