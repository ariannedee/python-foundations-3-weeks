"""
Hugging Face provides open-source AI models, with limited free usage (requires an account and API key).

https://huggingface.co/docs/inference-providers/guides/first-api-call
"""
from pprint import pprint

import requests

DEBUG = False

chat_history = []

with open('do_not_show.txt') as file:
    api_key = file.read().strip()

def query_huggingface_ai(prompt, model="meta-llama/Llama-3.2-3B-Instruct"):
    api_url = "https://router.huggingface.co/v1/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}"}

    chat_history.append({"role": "user", "content": prompt})

    payload = {
        "messages": chat_history,
        "model": model
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]

def send_message(prompt):
    content = query_huggingface_ai(prompt)
    chat_history.append(content)
    if DEBUG:
        pprint(chat_history)
    return content['content']

def start_chat():
    print("Start chatting with AI 🤖 (Q to quit)")

    while True:
        prompt = input("> ")
        if prompt.lower() == 'q':
            break
        response = send_message(prompt)
        print(response)

if __name__ == "__main__":
    start_chat()