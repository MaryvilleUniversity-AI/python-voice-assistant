import speech_recognition as sr
import webbrowser
import datetime
import time
import os

def respond(text):
    ''' This function handles the assistant's
        text-based 'response' '''
    print("Assistant:", text)

# Voice command logic
def callback(recognizer, audio):
    try:
        command = recognizer.recognize_google(audio).lower() # Converts spoken audio into text using Google's API
        print("You said:", command)

        # Check for specific keywords
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            respond(f"The time is {current_time}")
        elif "open google" in command: # Open Google in browser
            respond("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "open wikipedia" in command: # Open Wikipedia in browser
            respond("Opening Wikipedia.")
            webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
        elif "open youtube" in command: # Open YouTube in browser
            respond("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "play music" in command:
            respond("Playing your music.")
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=7TfV1MpnAtqQhvN4") # change path
        elif any(word in command for word in ['stop', 'exit', 'goodbye']): # Exit while loop
            respond("Goodbye! Have a great day.")
            # Stop background listener and exit program
            stop_listening(wait_for_stop=False)
            exit()
        else:
            respond("I didn't understand that command.")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Network error. Please check your connection.")

recognizer = sr.Recognizer() # Handles speech-to-text
mic = sr.Microphone() # Opens default input device

# Start program listening in a separate background thread.
stop_listening = recognizer.listen_in_background(mic, callback)

# Greeting
respond("Hello! I am your voice assistant. I am listening for commands now.")

# Keep program running
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt: # Allows manual stop with Ctrl + C
    speak("Goodbye!")
    stop_listening(wait_for_stop=False)