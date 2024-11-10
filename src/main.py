# main.py
import os
import time
from data_fetch import load_dataset, download_pdfs
from parsing import extract_text_from_pdf
from summarization import generate_summary
from key import extract_keywords
from docUpdation import update_mongo
from datetime import datetime

def process_documents():
    # Load dataset and download PDFs
    dataset = load_dataset()
    download_folder = "pdfs"
    download_pdfs(dataset, download_folder)

    # Process each PDF
    for name in dataset.keys():
        pdf_path = os.path.join(download_folder, f"{name}.pdf")
        if not os.path.exists(pdf_path):
            print(f"File {name} not found, skipping.")
            continue
        
        # Extract metadata
        metadata = {
            "name": name,
            "source_url": dataset[name],
            "size": os.path.getsize(pdf_path),
            "time_of_ingestion": datetime.utcnow()
        }

        # Start processing time tracking
        start_time = time.time()

        # Process PDF: Extract text, generate summary, extract keywords
        text = extract_text_from_pdf(pdf_path)
        summary = generate_summary(text)
        keywords = extract_keywords(text)
        
        # Calculate processing time
        processing_time = time.time() - start_time

        # Update MongoDB
        update_mongo(metadata, summary, keywords, processing_time)

if __name__ == "__main__":
    process_documents()
