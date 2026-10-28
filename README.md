# CareDesk — Hospital FAQ Assistant

A responsive full-stack web application based on the rule-based FAQ logic in the original `hospital_faq_chatbot.ipynb` notebook.

## Features

- Flask backend with `POST /api/chat` JSON endpoint
- Original Python fuzzy matching approach (`difflib.SequenceMatcher`)
- Responsive hospital help-chat UI
- Suggested questions, message timestamps, typing indicator, and clear-chat control
- Input validation and friendly fallback responses
- Basic automated tests

## Tech stack

- Python 3
- Flask
- HTML5, CSS3, vanilla JavaScript
- Python `unittest`

## Run locally (Windows)

1. Install Python 3.10 or newer.
2. Extract this ZIP and open the extracted folder in VS Code.
3. Open the terminal in that folder and create a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\\Scripts\\activate.bat`.

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Test

With the virtual environment activated, run:

```powershell
python -m unittest discover -s tests -v
```

## API example

Request:

```http
POST /api/chat
Content-Type: application/json
```

```json
{"message": "Where is the hospital located?"}
```

Response:

```json
{
  "reply": "The sample hospital is listed at Main Boulevard, Lahore, Pakistan. Please verify the address with the hospital before travelling.",
  "matched_question": "where is the hospital located",
  "confidence": 1.0
}
```

## Project structure

```text
hospital_faq_chatbot_webapp/
├── app.py
├── chatbot_engine.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/chat.js
└── tests/
    └── test_chatbot.py
```

## Important before publishing

This is an educational demo. The hospital name, address, phone number, email, service descriptions, and opening hours are sample details inherited from the original notebook or clarified as placeholders. Verify or replace them before presenting this as a real hospital service. Do not use the demo for diagnosis or medical advice. For emergencies, contact local emergency services.

## Deployment note

For production deployment, use a production WSGI server (such as Gunicorn on compatible hosts), set debug mode off, configure HTTPS, and review security/privacy requirements. Do not deploy Flask's development server.
