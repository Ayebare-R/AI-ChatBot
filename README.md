# Conversational AI Assistant

A simple Python chatbot that learns from user interactions. It matches user questions to a knowledge base, provides answers, and learns new responses when it doesn't recognize a query.

## How It Works
1. User enters a question
2. Bot finds closest match in knowledge base
3. If match found: Returns stored answer
4. If no match: Asks user to provide an answer
5. New Q&A pairs are saved to the knowledge base

## Requirements
- Python 3.x
- Standard libraries: `json`, `difflib`, `sys`, `time`

## Setup & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
2. Run the chatbot:
python your_filename.py