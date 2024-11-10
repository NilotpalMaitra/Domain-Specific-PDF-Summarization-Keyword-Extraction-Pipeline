from transformers import pipeline
import torch

# Check if a GPU is available
device = 0 if torch.cuda.is_available() else -1

# Initialize the summarizer on the GPU (device=0) or CPU (device=-1)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def generate_summary(text):
    try:
        # Log the input length for debugging
        print(f"Processing text of length: {len(text)}")
        
        # Skip empty or short texts to prevent errors
        if len(text.strip()) < 50:
            print("Text too short for summarization.")
            return "Text too short for summarization."

        # Limit text length to prevent overload
        text = text[:2000]  # Adjust limit as needed

        # Generate the summary
        summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("Summarization error:", e)
        return ""

