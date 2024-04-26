# Agriculture-chatbot-krushak
Agruculture chatbot based on Custom dataset and Google-Gemini-LLM

Sure, here's a basic README file for your project:

Krushak
Krushak is a Flask-based web application designed to provide agricultural information and assistance to users. It leverages the Gemini API for natural language generation and responds to user queries related to agriculture, crops, and farming practices.

Features
Natural Language Processing (NLP): Krushak utilizes NLTK for NLP tasks such as tokenization and word processing.
Gemini API Integration: Gemini API is integrated for generating natural language responses to user queries.
Crop Data: The application loads crop data from a CSV file and provides information based on user input.
User Interaction: Users can interact with Krushak by typing messages in the chat interface.
Dynamic Responses: Krushak provides dynamic responses based on user queries and the available crop data.
Setup
To run Krishibot locally, follow these steps:

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Ensure NLTK resources are downloaded using nltk.download('punkt').
Replace 'balaram1.csv' with your own crop data CSV file, ensuring it has the necessary columns.
Set up a Google API key and configure it in the environment or directly in the code.
Setup the virtual environment for the project.
Run the Flask application using python app.py.
Access the Krushak interface through your web browser.
Usage
Once Krushak is running, access the web interface and start typing messages in the chat window. Krishibot will respond to your queries with relevant agricultural information, crop details, and farming practices.

Contributing
Contributions to Krushak are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

