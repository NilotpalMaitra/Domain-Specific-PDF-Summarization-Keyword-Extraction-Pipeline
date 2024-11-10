# data_fetch.py
import json
import requests
import os

# Load the JSON dataset
def load_dataset(file_path="Dataset.json"):
    with open(file_path, 'r') as file:
        return json.load(file)

# Download PDFs from URLs in Dataset.json
# data_fetch.py

def download_pdfs(dataset, download_folder="pdfs"):
    os.makedirs(download_folder, exist_ok=True)
    for name, url in dataset.items():
        pdf_path = os.path.join(download_folder, f"{name}.pdf")
        try:
            response = requests.get(url, verify=False)  # Disable SSL verification
            response.raise_for_status()
            with open(pdf_path, 'wb') as file:
                file.write(response.content)
            print(f"{name} downloaded successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {name}: {e}")

