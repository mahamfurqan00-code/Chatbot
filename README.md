# Chatbot
# Hospital FAQ Assistant Chatbot

An intuitive, rule-based Python chatbot designed to answer common Frequently Asked Questions (FAQs) for **ABC General Hospital**. It leverages text normalization, substring checks, and fuzzy string matching (`SequenceMatcher`) to provide accurate responses even when user queries contain minor typos or varied phrasing.

---

## ✨ Features

* **Hospital Knowledge Base:** Pre-configured with responses for appointments, operating hours, doctor availability, emergency services, lab tests, payments, and location.
* **Text Normalization:** Cleans user inputs by lowercasing, removing special characters, and stripping extra whitespace.
* **Fuzzy Matching:** Uses Python's built-in `difflib.SequenceMatcher` to calculate text similarity scores, matching user questions intelligently.
* **Confidence Thresholding:** Filters out irrelevant queries using a configurable similarity threshold (`0.6`).
* **Interactive CLI Interface:** A simple command-line loop allowing real-time interaction.

---

## 📂 Project Structure

```text
.
├── hospital_faq_chatbot.ipynb   # Main Jupyter Notebook containing chatbot logic
└── README.md                    # Project documentation
