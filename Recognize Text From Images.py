import os
import pytesseract
import PIL.Image

def extract_text_from_image(file_path):
    # Initialize variable
    text = ""

    # Check if the file is an image
    if file_path.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
        try:
            image = PIL.Image.open(file_path)
            text = pytesseract.image_to_string(image)
        except Exception as e:
            print(f"Error processing image {file_path}: {str(e)}")

    return text

# Specify the directory path
path = r"path to folder containing the files"

# List all files in the directory and create their full paths
files = os.listdir(path)
full_paths = [os.path.join(path, filename) for filename in files]

# Iterate through each file (images) and extract text
for file_path in full_paths:
    extracted_text = extract_text_from_image(file_path)
    if extracted_text:
        print(f"Text extracted from {file_path}:\n{extracted_text}\n")