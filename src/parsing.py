# parsing.py
import fitz  # PyMuPDF
import os

def ingest_pdfs(folder_path):
    pdf_data_list = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            with fitz.open(os.path.join(folder_path, file_name)) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            pdf_data = {
                "text": text,
                "metadata": {
                    "name": file_name,
                    "size": os.path.getsize(os.path.join(folder_path, file_name)),
                    "time_of_ingestion": "timestamp_here"
                }
            }
            pdf_data_list.append(pdf_data)
    return pdf_data_list
