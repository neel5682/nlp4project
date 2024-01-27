import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def record_text():
    with sr.Microphone() as source:
        print("Say something:")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error connecting to Google Speech Recognition service: {e}")
            return ""

def speak_text(text):
    global engine
    
   
    if not engine._inLoop:
        engine.say(text)
        engine.runAndWait()


def output_text_to_file(text):
    with open("output.txt", "a") as file:
        file.write(text + "\n")

if __name__ == "__main__":
    while True:
        user_input = input("Press 'r' to record text, 's' to speak text, 'q' to quit: ").lower()

        if user_input == 'r':
            recorded_text = record_text()
            if recorded_text:
                output_text_to_file(recorded_text)
        elif user_input == 's':
            text_to_speak = input("Enter text to speak: ")
            speak_text(text_to_speak)
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Please enter 'r', 's', or 'q'.")
