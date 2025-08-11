import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key  = os.getenv("PERPLEXITY_API_KEY", "")

def get_perplexity_response(system_message: str, user_message: str) -> str:
    """
    Calls the Perplexity API with system and user messages.
    
    Args:
        system_message (str): The system instruction for the model.
        user_message (str): The user input/question.
        api_key (str): Your Perplexity API key.

    Returns:
        str: The content from the model's response.
    """
    
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Raise error for bad status codes
    data = response.json()

    # Extract and return the model's reply content
    return data["choices"][0]["message"]["content"]

# Example usage:
if __name__ == "__main__":
    system_msg = "You are riddle solver, crack the riddles and provide just the answer"
    user_msg = "I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?"

    try:
        content = get_perplexity_response(system_msg, user_msg)
        print("Model Response:", content)
    except requests.exceptions.RequestException as e:
        print("Error calling Perplexity API:", e)