import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def ask_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["response"]

    return "Erro ao consultar o modelo."