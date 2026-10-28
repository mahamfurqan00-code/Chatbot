# Hospital FAQ Chatbot

## About the Project

The Hospital FAQ Chatbot is a simple web-based chatbot designed to help users find answers to common hospital-related questions. Instead of searching through different pages or waiting for someone to respond, users can ask a question and get a relevant answer directly through the chatbot.

I developed this project using Python and Flask for the backend, along with HTML, CSS, and JavaScript for the frontend. The chatbot uses text matching techniques to understand user questions and find the closest matching answer from a predefined set of frequently asked questions.

This project helped me practice Python programming, web development, API integration, and building a user-friendly interface.

## Features

- Interactive and user-friendly chat interface.
- Instant responses to common hospital-related questions.
- Python-based chatbot logic.
- Fuzzy text matching to handle slightly different question wording.
- Flask backend with a chat API.
- Suggested questions to help users get started.
- Responsive design for desktop and mobile screens.
- Fallback responses when the chatbot cannot find a suitable answer.
- Basic automated tests for chatbot functionality.

## Technologies Used

- **Python** – Chatbot logic and backend functionality.
- **Flask** – Web framework for handling requests and responses.
- **HTML** – Structure of the web interface.
- **CSS** – Styling and responsive layout.
- **JavaScript** – Chat interactions and communication with the backend.
- **SequenceMatcher** – Finding similar questions using text similarity.
- **Unittest** – Testing the chatbot functionality.

## Project Structure

```text
Hospital-FAQ-Chatbot/
│
├── app.py
├── chatbot_engine.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── chat.js
│
└── tests/
    └── test_chatbot.py
```

## Getting Started

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/mahamfurqan00-code/Chatbot.git
```

### 2. Open the Project Folder

```bash
cd Chatbot
```

Make sure the project files are extracted into this folder if you downloaded the project as a ZIP file.

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Once the server starts, open the following address in your browser:

```text
http://127.0.0.1:5000
```

You can now interact with the chatbot through the web interface.

## Running Tests

To run the automated tests, use:

```bash
python -m unittest discover -s tests -v
```

These tests help check the chatbot's responses and basic functionality.

## How It Works

1. The user enters a question in the chat interface.
2. JavaScript sends the question to the Flask backend.
3. The chatbot processes the text and compares it with predefined FAQ questions.
4. The text-matching logic identifies a suitable response when a sufficiently close match is found.
5. The backend returns the answer to the frontend.
6. The answer appears in the chat window.

If the chatbot cannot find a suitable match, it provides a fallback response instead of guessing an answer.

## What I Learned

While working on this project, I gained practical experience in connecting a Python backend with a web-based frontend. I also learned how to create API endpoints, handle user input, work with text similarity, and organize a Flask application into separate files.

One of the main things I explored was how a chatbot can match questions even when users phrase them differently.

## Future Improvements

There are several ways this project could be improved in the future:

- Add more hospital FAQs and allow easier updates to the FAQ database.
- Integrate a database to store FAQs and chat history.
- Improve question matching using Natural Language Processing (NLP).
- Add multilingual support.
- Include an admin panel for managing questions and answers.
- Deploy the application so it can be accessed online.

## Important Note

This project is intended for educational and informational purposes. It does not provide medical diagnoses or replace professional medical advice. Hospital contact details and other sample information should be verified before real-world use.

## Author

**Maham Furqan**

GitHub: [mahamfurqan00-code](https://github.com/mahamfurqan00-code)

---

Thanks for checking out my project! I'm continuously learning and improving my Python and web development skills through hands-on projects.
