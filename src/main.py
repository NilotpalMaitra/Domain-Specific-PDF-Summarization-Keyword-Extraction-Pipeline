
import os
from parsing import ingest_pdfs
from summarization import generate_summary
from keyword import extract_keywords
from docUpdation import update_mongo

def main(folder_path):
    pdfs = ingest_pdfs(folder_path)
    
    for pdf_data in pdfs:
        doc_text = pdf_data['text']
        
        # Generate a summary
        summary = generate_summary(doc_text)
        
        # Extract keywords
        keywords = extract_keywords(doc_text)
        
        # Update MongoDB with results
        update_mongo(pdf_data['metadata'], summary, keywords)

if __name__ == "__main__":
    folder_path = "path/to/pdf/folder"  # Update with your folder path
    main(folder_path)
