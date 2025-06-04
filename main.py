from pdf_reader import extract_text_from_pdf
from gemini_chat import ask_gemini_about_pdf

def main():
    # Get PDF file path
    pdf_path = "C:/Users/Siyumi Jayawardhane/OneDrive - Informatics Institute of Technology/Certificates/Oral_Cancer_Risk_Presdiction_Chatbot/Group 33.pdf"
    pdf_text = extract_text_from_pdf(pdf_path)

    print("\nPDF loaded. You can now ask questions!\n")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = ask_gemini_about_pdf(pdf_text, question)
        print(f"Gemini: {answer}\n")

if __name__ == "__main__":
    main()
