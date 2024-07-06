import sys
import json
from typing import Optional

import requests
from rich.console import Console
from rich.markdown import Markdown

console = Console()

API_KEY = "..." # You can get it from https://console.groq.com/keys

def generate_groq_prompt(prompt: str, model: str="llama3-70b-8192") -> Optional[str]:
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        history = [{'role': 'user', 'content': prompt}]

        data = {
            "model": model,
            "messages": history,
            "max_tokens": 2048,
            "n": 1,
            "temperature": 0.9,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            response = response_data['choices'][0]['message']['content']

            return response
        else:
            return
    except:
        return


console.print('Assistant: Hello and welcome.! How can I assist you today?', style='cyan')

@lambda _: _()
def process_user_input() -> None:
    error_message = (
        "Sorry, I'm unable to assist with that particular request. "
        "If there's anything else you need help with, please feel free to let me know!"
    )
    while True:
        prompt = input()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K') 
        console.print(f"User: {prompt}", style='yellow')
        response = generate_groq_prompt(prompt)

        if response is not None:
            console.print(Markdown(f"Assistant: {response}"), style='cyan')
        else:
            console.print(error_message, style='cyan')
