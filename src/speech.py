import sounddevice as sd
import numpy as np
import speech_recognition as sr
import scipy.io.wavfile as wav

def listen(duration=5, fs=16000):
    print("🎤 Ouvindo...")

    # grava áudio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    filename = "temp_audio.wav"
    wav.write(filename, fs, recording)

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text

    except sr.UnknownValueError:
        print("Não entendi.")
        return None

    except Exception as e:
        print(f"Erro: {e}")
        return None