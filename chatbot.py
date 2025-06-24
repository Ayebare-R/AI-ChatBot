import json
from difflib import get_close_matches
import sys
import time

EXIT_COMMANDS = ["end", "quit", "bye", "goodbye", "done"]

def load_data_store(file_path: str) -> dict:
    """Load conversational data from JSON file"""
    with open(file_path) as file:
        return json.load(file)

def update_data_store(file_path: str, data: dict):
    """Save updated conversational data to JSON file"""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_closest_query(user_input: str, questions: list) -> str:
    """Identify the closest matching question from dataset"""
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_corresponding_answer(query: str, data: dict) -> str:
    """Retrieve answer for specified question from dataset"""
    for item in data["questions"]:
        if item["question"] == query:
            return item["answer"]

def display_with_typing_effect(text: str):
    """Print text with simulated typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def start_conversation():
    """Initiate interactive conversation interface"""
    knowledge_base = load_data_store("./database.json")
    unknown_response = "I do not know what that means :( - please help me learn."
    learning_prompt = "Please type the answer, or 'skip' to skip."
    learning_confirmation = "Thank you for teaching me something new! Now I know :) "
    
    while True:
        user_message = input("You: ")
        if user_message.lower() in EXIT_COMMANDS:
            break
            
        existing_questions = [q["question"] for q in knowledge_base["questions"]]
        closest_match = find_closest_query(user_message, existing_questions)
        
        if closest_match:
            bot_response = get_corresponding_answer(closest_match, knowledge_base)
            display_with_typing_effect("Bot: " + bot_response)
        else:
            display_with_typing_effect("Bot: " + unknown_response)
            display_with_typing_effect(learning_prompt)
            new_answer = input()
            
            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({
                    "question": user_message,
                    "answer": new_answer
                })
                update_data_store(
                    "/Users/chipiro/Desktop/random/ai/knowledge_base.json",
                    knowledge_base
                )
                display_with_typing_effect(learning_confirmation)

if __name__ == "__main__":
    start_conversation()