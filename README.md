# LLM Smart Assistant

A simple command-line chatbot built with Python and the Google Gemini API. This project demonstrates how to use a system prompt to control an AI's behavior.

---
## Features ✨

* Provides clear, step-by-step answers.
* Explains the reasoning behind its responses.
* Politely refuses to perform mathematical calculations.

---
## Setup

1.  **Install Libraries:**
    Open your terminal and run this command:
    ```bash
    pip install google-generativeai python-dotenv
    ```

2.  **Add API Key:**
    Create a new file in the same project folder and name it `.env`. Inside this file, add your API key like this:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

---
## How to Run

Execute the script from your terminal:
```bash
python chatbot.py
