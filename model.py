import joblib

model = joblib.load("NBSpamDetector3.pkl") # Load model

vectorizer = joblib.load("cv3.pkl") # Load vectoriser 

def predict_spam(text): #Define spam preditcting function

    text_vector = vectorizer.transform([text]) # convert text to numerical format
    prediction = model.predict(text_vector) # Make a prediction 
    if prediction == 1:
        return "This is Spam! Delete Email at ONCE!" # Return string, displayed in the HTML 
    else:
        return "This is Ham! Keep the email! (Could be important!) "  # Return string, displayed in the HTML 


