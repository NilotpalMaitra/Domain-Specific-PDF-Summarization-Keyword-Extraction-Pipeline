
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_keywords(text, max_keywords=5):
    # Tokenize and clean text
    words = re.findall(r'\w+', text.lower())
    tfidf = TfidfVectorizer(max_features=max_keywords, stop_words='english')
    tfidf.fit_transform([' '.join(words)])
    
    # Extract keywords
    keywords = tfidf.get_feature_names_out()
    return list(keywords)
