from .speech import listen
from .assistant import ask_ollama
from .tts import speak


def run_assistant():
    print("Assistente iniciado. Pode falar.")

    while True:
        text = listen()

        if not text:
            continue

        response = ask_ollama(text)

        print(f"Resposta: {response}")

        speak(response)