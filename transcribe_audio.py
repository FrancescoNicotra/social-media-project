import speech_recognition as sr
import pandas as pd

def transcribe_audio(audio_path, csv_path):
    recognizer = sr.Recognizer()

    # Carica l'audio
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    # Prova a trascrivere tutto l'audio
    try:
        text = recognizer.recognize_google(audio_data, language="en-US")

        # Crea un DataFrame con una sola riga
        df = pd.DataFrame({'testo': [text]})

        # Salva il DataFrame nel file CSV
        df.to_csv(csv_path, index=False, encoding='utf-8')
    except sr.UnknownValueError:
        print("Il riconoscimento vocale non è riuscito a capire l'audio.")
    except sr.RequestError as e:
        print(f"Errore nel servizio di riconoscimento vocale: {e}")

if __name__ == "__main__":
    audio_path = './audio/Chris_Evans_OPENS_UP_About_His_‘Deadpool_&_Wolverine’_Cameo_(Exclusive)__E!_News.wav'
    csv_path = './transcriptions.csv'

    transcribe_audio(audio_path, csv_path)