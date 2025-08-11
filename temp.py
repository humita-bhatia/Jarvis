# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone(device_index=0) as source:  # Use your mic's index
#     print("Listening...")
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Sorry, I could not understand.")
# except sr.RequestError:
#     print("Could not request results, check your internet connection.")


import os
def speak(text):
    os.system(f"say '{text}'")
speak("hey")