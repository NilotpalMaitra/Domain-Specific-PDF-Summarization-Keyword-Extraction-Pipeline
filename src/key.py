# keyword.py
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_keywords(text, max_keywords=5):
    words = re.findall(r'\w+', text.lower())
    tfidf = TfidfVectorizer(max_features=max_keywords, stop_words='english')
    tfidf.fit_transform([' '.join(words)])
    return list(tfidf.get_feature_names_out())
