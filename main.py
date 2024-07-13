import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, my speech service is down."

if __name__ == "__main__":
    while True:
        print("Say something!")
        speech = recognize_speech()
        print(f"You said: {speech}")
        speak(f"You said: {speech}")
        if "exit" in speech.lower():
            speak("Goodbye! we will meet you again")
            break
