import os
import chardet
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from flask import Flask, render_template, request
from dotenv import load_dotenv


# Import gemini and necessary modules
import google.generativeai as genai


# Initialize Flask app
app = Flask(__name__)

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Detect encoding of the CSV file
with open('balaram1.csv', 'rb') as f:
    result = chardet.detect(f.read())

# Load your CSV file
crop_data = pd.read_csv('balaram1.csv', encoding=result['encoding'])

# Define rules for different categories
rules = {
    "greeting": {"keywords": ["hello", "hi", "hey"], "response": "Hello! How can I help you today?"},
    "farewell": {"keywords": ["bye", "goodbye", "exit"], "response": "Goodbye! Have a great day!"},
    "unknown": {"response": "I'm sorry, I couldn't understand your query. Can you please rephrase it?"},
}

# Attributes to be recognized as keywords
target_attributes = list(crop_data.columns)

# Configure Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

# Function to process user input and generate response
def process_input(user_input):
    words = word_tokenize(user_input.lower())

    # Check for farewell keyword
    for category, rule in rules.items():
        if "keywords" in rule:
            if any(keyword in words for keyword in rule["keywords"]):
                return rule["response"]

    # Extract attribute and crop name from user input
    attribute = None
    crop_names = []  # Initialize an empty list to store crop names

    # Iterate through all words in the input
    for word in words:
        if word in target_attributes:  # Check if the word is an attribute
            attribute = word
        elif word in crop_data['crop_name'].str.lower().values:  # Check if the word is a crop name
            crop_names.append(word)  # Append crop name to the list

    # Generate response based on extracted information
    if crop_names:
        # If crop names are identified, check for attribute or provide general information
        if attribute:
            responses = []
            for crop_name in crop_names:
                try:
                    value = crop_data.loc[crop_data['crop_name'].str.lower() == crop_name, attribute].values[0]
                    responses.append(f"{value}")
                except IndexError:
                    responses.append(model.generate_content(user_input,stream=True).text)
            return '\n'.join(responses)
        else:
            # If input is not recognized, use Gemini model to generate response
            return model.generate_content(user_input).text
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    # return process_input(input_text)
    response = process_input(input_text)
        # Otherwise, return the response as a string
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
