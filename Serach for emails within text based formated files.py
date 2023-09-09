import os
import PyPDF2
import textract

def extract_emails_from_document(file_path):
    # Initialize variables
    emails = []
    text = ""

    # Check the file type and process accordingly
    if file_path.endswith((".docx", ".pptx", ".txt")):
        try:
            text = textract.process(file_path).decode("utf8")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    elif file_path.endswith(".pdf"):
        try:
            with open(file_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    text += page_text
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    # Extract emails from the text
    emails.extend([word for word in text.split() if "@" in word])

    return emails

# Specify the directory path
path = r"path to folder containing the files to be processed"

# List all files in the directory and create their full paths
files = os.listdir(path)
full_paths = [os.path.join(path, filename) for filename in files]

# Iterate through each file (documents) and extract emails
for file_path in full_paths:
    extracted_emails = extract_emails_from_document(file_path)
    if extracted_emails:
        print(f"Emails found in {file_path}:\n{', '.join(extracted_emails)}\n")
