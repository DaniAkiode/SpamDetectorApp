import joblib

# Load vectorizer
vectorizer = joblib.load("cv3.pkl")
TFVectorizer = joblib.load("tfidf.pkl")

# Load multiple models
models = {
    "naive_bayes": joblib.load("NBSpamDetector3.pkl"),
    "random_forest": joblib.load("rfBasedSpamDetector.pkl"),  
}

def predict_spam(text, model_name="naive_bayes"):  # Default to Naive Bayes
    if model_name not in models:
        return "Invalid model selected!"

    model = models[model_name]  # Get selected model
    text_vector = vectorizer.transform([text])  # Convert text to numerical format
    prediction = model.predict(text_vector)  # Make a prediction
    
    if prediction == 1:
        return "This is Spam! Delete Email at ONCE!"
    else:
        return "This is Ham! Keep the email! (Could be important!)"







"""model = joblib.load("NBSpamDetector3.pkl") # Load model

vectorizer = joblib.load("cv3.pkl") # Load vectoriser 

def predict_spam(text): #Define spam preditcting function

    text_vector = vectorizer.transform([text]) # convert text to numerical format
    prediction = model.predict(text_vector) # Make a prediction 
    if prediction == 1:
        return "This is Spam! Delete Email at ONCE!" # Return string, displayed in the HTML 
    else:
        return "This is Ham! Keep the email! (Could be important!) "  # Return string, displayed in the HTML 

"""
