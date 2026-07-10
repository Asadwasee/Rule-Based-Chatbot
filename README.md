# Rule-Based AI Chatbot

An intelligent, lightweight, and highly efficient rule-based AI chatbot developed as part of the **DecodeLabs Internship Program (Week 1 Project)**.

## Description
This project implements a classic rule-based conversational agent using pure Python. Instead of using resource-heavy deep learning libraries or inefficient, hard-to-maintain `if-elif` conditional ladders, this chatbot utilizes a **Python Dictionary (Hash Map)** structure to match user intents instantly with O(1) time complexity.

### Key Features:
* **Continuous Execution Loop:** Runs seamlessly in a continuous execution loop until a specific exit command is triggered.
* **Input Sanitization & Normalization:** Automatically processes user messages using `.lower()` and `.strip()` to prevent case-sensitivity or leading/trailing spacing issues.
* **Smart Fallback Mechanism:** Uses the dictionary `.get()` method to elegantly handle unknown queries with a default response without crashing.
* **Clean Exit Strategy:** Safely terminates the execution loop and closes the program when the user types 'exit' or 'bye'.

---

## Project Structure
* `chatbot.py` - The main Python script containing the chatbot logic and knowledge base.
* `README.md` - Complete project documentation and execution guide.

---

## How to Run

### Prerequisites
Make sure you have Python installed on your system. You can verify your installation by running this command in your terminal:
```bash
python --version

Steps to Execute
Open your terminal, command prompt, or VS Code terminal inside the project folder.

Run the chatbot script using the following command:

Bash
python chatbot.py

Interact with the chatbot by typing keywords like hello, products, payment, status, or help.

Type exit or bye to cleanly stop the program.
