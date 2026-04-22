import re
import string
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

# Load model
model = joblib.load("model/svm_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# NLP setup
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

# Preprocess
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()  

    cleaned = [
        lemmatizer.lemmatize(w)
        for w in words
        if w not in stop_words
    ]

    return ' '.join(cleaned)

# Department prediction
def predict_department(text):
    clean = preprocess_text(text)
    vec = vectorizer.transform([clean])

    pred = model.predict(vec)[0]

    print("Prediction value:", pred)  # inside function

    return str(pred)

    return str(pred)   

# Sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']

    if score < -0.6:
        return "Critical", 5
    elif score < -0.2:
        return "Negative", 3
    else:
        return "Normal", 1

# Final function
def analyze_text(text):
    dept = predict_department(text)
    sentiment, priority = get_sentiment(text)

    return {
        "department": dept,
        "sentiment": sentiment,
        "priority_score": priority
    }
