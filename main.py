from .speech import listen
from .tts import speak
from .assistant import process_command

def run_assistant():
    speak("Assistente iniciado. Pode falar.")

    while True:
        command = listen()

        if command:
            if "sair" in command.lower():
                speak("Encerrando assistente.")
                break

            response = process_command(command)
            speak(response)