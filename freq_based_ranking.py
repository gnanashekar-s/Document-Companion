from PyPDF2 import PdfFileReader
import os

# Function to extract and store PDF texts in a dictionary
def extract_pdf_text(folder_paths):
    pdf_texts = {}
    
    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            print(root,files)
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            pdf = PdfFileReader(f)
                            text = ""
                            for page_num in range(pdf.getNumPages()):
                                page = pdf.getPage(page_num)
                                text += page.extractText()

                            # Store the file's text in the dictionary
                            pdf_texts[file_path] = text

                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

    return pdf_texts


# Function to search for keywords in the pre-extracted text dictionary
def search_in_pdf_texts(pdf_texts, keyword):
    search_results = {}
    ranking = {}
    
    for file_path, text in pdf_texts.items():
        frequency = text.lower().count(keyword.lower())
        
        if frequency > 0:
            search_results[file_path] = frequency

    if search_results:
        # Sort the results by frequency in descending order
        ranking = {k: v for k, v in sorted(search_results.items(), key=lambda item: item[1], reverse=True)}
    
    return ranking
