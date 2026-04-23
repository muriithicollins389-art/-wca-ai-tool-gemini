import json
import requests
import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_txt(txt_path):
    """Extract text from TXT file"""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading text file: {e}")
        return ""
def summarize_report():
    # --- API CONFIGURATION FOR OPENAI ---
    API_KEY = "process.env.API KEY"
    API_URL = "https://api.openai.com/v1/chat/completions"

    # --- USER INPUT METHOD SELECTION ---
    print("--- Report Summarizer Tool ---")
    print("Choose input method:")
    print("1. Paste text directly")
    print("2. Upload PDF file")
    print("3. Upload TXT file")
    
    
    
    report_text = ""
    
    if choice == '1':
        # Direct text paste
        print("\nPaste your report below:")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        
    
    elif choice == '2':
        # PDF file upload
        pdf_path = input("Enter PDF file path: ").strip().strip('"').strip("'")
        if os.path.exists(pdf_path):
            print("Extracting text from PDF...")
            report_text = extract_text_from_pdf(pdf_path)
            if report_text:
                print(f"Successfully extracted {len(report_text)} characters")
            else:
                print("Could not extract text from PDF")
        else:
            print("File not found!")
            return
    
    elif choice == '3':
        # TXT file upload
        txt_path = input("Enter TXT file path: ").strip().strip('"').strip("'")
        if os.path.exists(txt_path):
            print("Reading text file...")
            report_text = extract_text_from_txt(txt_path)
            if report_text:
                print(f"Successfully read {len(report_text)} characters")
            else:
                print("Could not read text file")
        else:
            print("File not found!")
            return
    
    else:
        print("Invalid choice!")
        return
    
    if not report_text.strip():
        print("No text to summarize. Exiting.")
        return
       # --- DESIGNED PROMPT ---
    system_instruction = (
        f"Role: Expert Executive Assistant. "
        f"Task: Summarize the text in a professional tone. "
        f"Context: User is preparing for a meeting. "
        f"Return ONLY valid JSON. "
        f'Output Format: {{"title": str, "summary": str, "action_items": list}}'
    )
          # API INTEGRATION FOR OPENAI ---
    
    if len(report_text) > 1000:
        print(f"Text is long ({len(report_text)} chars), truncating to first 12000 chars")
        report_text = report_text[:1000]
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": report_text}
        ],
        "response_format": {"type": "json_object"}
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
