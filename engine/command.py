import pyttsx3
import speech_recognition as sr
import eel
import threading#idk whyyes
# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"


def speak(text):
    engine = pyttsx3.init('nsss' )#nsss for mac and sapi5 for windows
    for voice in engine.getProperty('voices'):
        if "Daniel" in voice.name:
            engine.setProperty('voice', voice.id)
            engine.setProperty('rate',170)
            break
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@eel.expose
def takecommand():
    print("🔹 takecommand() called from JS")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Speech recognition error:", e)
        return ""
    return query.lower()







# @eel.expose
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source,10,6)
#     try:
#         print('Recognizing...')
#         query=r.recognize_google(audio,language="en-in")
#         print(f"User siad: {query}")
#     except Exception as e:
#         print(e)
#         return ""
#     return query.lower()


'''
speaks what you said 
text=takecommand()
speak(text)
'''
# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# for idx, voice in enumerate(voices):
#     print(f"{idx}: {voice.name} ({voice.id})")




'''
14-male good uk*** Daniel
82-siri female ** Karen
132-siri female * Samantha 
117- indian male Rishi
87-indian female Lekha
96-female Moira 
100, 174-robot Organ and Zarvox
105/18-real robot Reed and Eddy            
'''


'''
import pyttsx3

def speak(text, voice_index=0):
    engine = pyttsx3.init('nsss')  # 'nsss' for macOS
    voices = engine.getProperty('voices')
    
    # Optional: Print available voices
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} ({voice.id})")
    
    # Safely set the voice if the index is in range
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    else:
        print("Voice index out of range, using default.")
    
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am testing voice number .", voice_index=9)
'''