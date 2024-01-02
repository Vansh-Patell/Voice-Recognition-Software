# Check if the users have the required libraries installed.
import importlib
import subprocess
import webbrowser
import speech_recognition as sr


# Create a recognizer object
recognizer = sr.Recognizer()

#Capturing Voice Input - This function will capture the voice input from the microphone
def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def install_package(package_name):
    subprocess.check_call(['pip', 'install', package_name])


# Converting Voice Input to Text - This function will convert the captured voice input to text
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

#Processing Voice Commands 
def process_voice_command(text):

    
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    elif "tell me a joke" in text.lower():
        print("Why don't scientists trust atoms? Because they make up everything!")
    elif "open the browser" in text.lower():
        print("Opening the browser...")
        webbrowser.open("http://www.google.com")
    elif "play music" in text.lower():
        print("Playing music...")
        webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")

    else:
        print("I didn't understand that command. Please try again.")
    return False

# Libraries to check: SpeechRecognition, PyAudio
def check_and_install_libraries():
    required_libraries = ['SpeechRecognition', 'PyAudio']

    for library in required_libraries:
        try:
            importlib.import_module(library)
            print(f"{library} is already installed.")
        except ImportError:
            print(f"{library} is not installed. Installing...")
            install_package(library)

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)            

if __name__ == "__main__":
    check_and_install_libraries()
    main()
