import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def process_command(command):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": command,
                "stream": False
            }
        )

        data = response.json()
        return data.get("response", "Não consegui responder.")
    
    except Exception as e:
        return f"Erro ao conectar ao Ollama: {e}"