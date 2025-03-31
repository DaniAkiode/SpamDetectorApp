from flask import Flask, request, render_template # for sending/getting data and 
from model import predict_spam # spam detection function
from database import create_table, insert_result  # import database functions 

app = Flask(__name__)

# Create table when app starts 

create_table()

@app.route("/", methods=["GET", "POST"]) #handles requests in homepage 
def index():
    result = None # Initialise result as None 
    if request.method == "POST": # Use POST to send data to the server 
        user_input = request.form.get("message") # Use '.get()' to avoid erros
        if user_input: #Make sure input is not empty
            result = predict_spam(user_input) # Get prediction
            insert_result(user_input, result)
        else:
            result = "No message entered!" # Handle empty input
    return render_template("index.html", result=result) # Render html templete with result

if __name__ == "__main__": # Runs only when this file is executed directly
    app.run(debug=True) # Enable debug mode 