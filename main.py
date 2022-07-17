import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()

while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=5)

            o = r.recognize_google(audio, language="de-DE")
            translation = translator.translate(o, src="de", dest="en")
            print(f"[{translation.origin}] -> {translation.text}")

    except Exception as e:
        print(e)