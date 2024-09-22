
import speech_recognition as sr

AUDIO_FILE = "Enefit_lenktynes.wav"
recognizer = sr.Recognizer()


# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data,language='lt-LT')
            with open('Enefit_lenktynes_tekstas.txt', 'w', encoding='utf-8') as f:
                f.write(text)

        except:
            print("error")


