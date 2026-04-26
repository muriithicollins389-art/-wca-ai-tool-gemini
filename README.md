WRITTEN REPORT STRUCTURE 
Report Summarizer Tool 
 
1.	Cover Page 
Group Name: GEMINI 
Member Names: 0715, ,0955,0388,3626,3968.
GitHub Link: https://github.com/muriithicollins389-art/-wca-ai-tool-gemini
Tool Name: AI Report Summarizer 


2.	Problem Statement 
What problem does your tool solve? 
Professionals, students, and researchers often face information overload when dealing with lengthy reports, research papers, and documents. Reading entire documents to extract key information is time-consuming and inefficient. 
Who benefits? 
•	Business professionals who need quick meeting preparation 
•	Students reviewing multiple research papers 
•	Researchers scanning literature efficiently 
•	Managers who receive numerous reports daily 
 
  
3.	Tool Description 
What does it do? 
The AI Report Summarizer is a command-line Python tool that: 
•	Accepts text input via three methods (direct paste, PDF upload, TXT upload) 
•	Extracts text from uploaded documents 
•	Sends content to OpenAI's GPT-3.5 Turbo API 
•	Returns a structured JSON response with: 
o	Document title 
o	Professional summary o 	Actionable items list 
How does a user interact with it? 
1.	Run the script: python summarizer.py 
2.	Choose input method (1, 2, or 3) 
3.	Provide text or file path 
4.	Receive formatted summary with title, summary, and action items 
4. AI Instruction Design Full R-T-C-C-O Prompt: 
text 
Role: Expert Executive Assistant 
Task: Summarize the text in a professional tone 
Context: User is preparing for a meeting 
Output Format: {"title": str, "summary": str, "action_items": list} 	
Explanation and Justification: 		
Component 	Purpose 	Why it works 
Role (Expert Executive Assistant) 	Defines AI's persona 	Executive assistants are trained to extract key information prioritize action items 
Task (Summarize in professional tone) 	Specifies core function 	Professional tone ensures credibility for business/academ contexts 
Context (Meeting preparation) 	Provides situational awareness 	Helps AI focus on actionable, relevant information 
Output Format (JSON with title, summary, action_items) 	Enforces structured response 	Makes output predictable and easy to parse programmatic
  
 
5.	Technical Overview 
How the Python Code Works: 
python 
# 1. Text Extraction Functions def extract_text_from_pdf(pdf_path): 
    """Uses PyPDF2 to read each page and extract text"""     with open(pdf_path, 'rb') as file: 
        pdf_reader = PyPDF2.PdfReader(file)         for page in pdf_reader.pages:             text += page.extract_text() 
 
# 2. API Configuration 
API_URL = "https://api.openai.com/v1/chat/completions" payload = { 
    "model": "gpt-3.5-turbo", 
    "messages": [system_instruction, user_content], 
    "response_format": {"type": "json_object"} 
} 
 
# 3. Response Handling response = requests.post(API_URL, headers=headers, json=payload) ai_content = json.loads(response.json()['choices'][0]['message']['content']) 
Key Components: 
Component 	Technology 	Purpose 
PDF parsing 	PyPDF2 	Extract text from PDF files 
API communication 	requests library 	Send/receive data to OpenAI 
Data handling 	JSON 	Parse structured responses 
Text truncation 	String slicing 	Handle long documents (1200 char limit) 
 
6. Challenges & Solutions 	
Challenge 	Solution 
Missing API key 	User must obtain from OpenAI platform and insert in code 
PDF extraction errors 	Added try-except blocks with user-friendly error messages 
Long documents exceeding token limits 	Implemented text truncation to first 1200 characters 
User input EOF handling 	Used try-except with EOFError for multi-line paste 
File path with quotes 	Added .strip('"').strip("'") to clean paths 
Incomplete tone selection 	Noted as incomplete feature (tone_choice variable unused) 
  
7. Ethics Reflection Potential Concerns: Bias Concerns
Potential Issues:
•	Language bias: GPT-3.5 may perform better with English text than other languages
•	Cultural bias: Professional tone definition varies by culture but tool assumes Western business norms
•	Domain bias: Model may be more accurate for common topics (business, tech) than niche fields
Potential concerns		
Concern 	Risk Level 	Mitigation 
API Key exposure 	High 	Advise users to use environment variables, not hardcode 
Data privacy 	Medium 	Documents sent to OpenAI servers; avoid sensitive data 
Summary bias 	Medium 	AI may emphasize certain perspectives; verify critical info 
Over-reliance on AI 	Medium 	Tool is assistive, not replacement for human judgment 
Cost implications 	Low 	API calls incur charges per token 
Recommendations: 
•	Never upload confidential or PII-containing documents 
•	Review summaries against original for critical decisions 
•	Use environment variables for API key: os.getenv("OPENAI_API_KEY") 
 
8.	Conclusion & Future Improvements 
Conclusion: 
The AI Report Summarizer successfully demonstrates how LLMs can automate document summarization, saving users significant time. The three input methods provide flexibility, and JSON output enables future automation. 
Future Improvements with More Time: 

1.	Longer document support - Implement chunking for >1200 characters 
2.	Batch processing - Summarize multiple documents at once 
3.	Progress bar - Visual feedback during processing 
4.	Local LLM option - Use open-source models for privacy 
5.	Custom length control - User-adjustable summary length 
6.	Caching - Avoid re-summarizing identical documents 
  
9.	Appendix — Full Source Code 
	import json
	import requests
	import PyPDF2
	import os
	from dotenv import load_dotenv
	
	# Load environment variables from .env file
	load_dotenv()
	
	def extract_text_from_pdf(pdf_path):
	    """Extract text from PDF file"""
	    text = ""
	    try:
	        with open(pdf_path, 'rb') as file:
	            pdf_reader = PyPDF2.PdfReader(file)
	            for page in pdf_reader.pages:
	                text += page.extract_text() + "\n"
	        return text	    except Exception as e:
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
	    #  API CONFIGURATION FROM ENVIRONMENT VARIABLES 
	    API_KEY = os.getenv("OPENAI_API_KEY")
	    if not API_KEY:
        print("Error: OPENAI_API_KEY not found in environment variables!")
        print("Please create a .env file with your API key or set the environment variable.")
        return
        API_URL = "https://api.openai.com/v1/chat/completions"

    #  USER INPUT METHOD SELECTION 
	    print("--- Report Summarizer Tool ---")
	    print("Choose input method:")
	    print("1. Paste text directly")
	    print("2. Upload PDF file")
    print("3. Upload TXT file")
	    
          choice = input("Enter choice (1/2/3): ").strip()
	    
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
	        report_text = "\n".join(lines)
	    
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
	    
	    tone_choice = input("\nProfession, casual,technical").strip() 
	
	    #  DESIGNED PROMPT 
	    system_instruction = (
	        f"Role: Expert Executive Assistant. "
	        f"Task: Summarize the text in a  {tone_choice}tone. "
	        f"Context: User is preparing for a meeting. "
	        f"Return ONLY valid JSON. "
	        f'Output Format: {{"title": str, "summary": str, "action_items": list}}'
	    )
	
	    #  API INTEGRATION FOR OPENAI 
	    
	    if len(report_text) > 1200:
	        print(f"Text is long ({len(report_text)} chars), truncating to first 12000 chars")
	        report_text = report_text[:1200]
	    
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
	
	    try:
    		        print("\nSending to OpenAI for summarization...")
	        response = requests.post(API_URL, headers=headers, json=payload)
	        print(f"API Response Status: {response.status_code}")
	        response.raise_for_status()
	        
	        raw_data = response.json()
	        ai_content = json.loads(raw_data['choices'][0]['message']['content'])	
	        print("\n** REPORT SUMMARY **")
	        print(f"Title: {ai_content.get('title', 'N/A')}")
	        print(f"Summary: {ai_content.get('summary', 'N/A')}")
	        print("Action Items:")
	        for item in ai_content.get('action_items', []):
	            print(f"- {item}")
	
	    except Exception as e:
	        print(f"An error occurred: {e}")
	        if 'response' in locals():
	            print(f"Response text: {response.text}")
	
	if __name__ == "__main__":
	    summarize_report()
	


