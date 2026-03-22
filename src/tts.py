import pyttsx3

engine = pyttsx3.init()

# configurações de voz
engine.setProperty("rate", 180)  # velocidade da fala
engine.setProperty("volume", 1)  # volume (0 a 1)

def speak(text):
    print(f"Assistente: {text}")
    engine.say(text)
    engine.runAndWait()