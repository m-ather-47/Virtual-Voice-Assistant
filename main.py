import random
import sys
import webbrowser as wb
from datetime import datetime as dt
import pyttsx3 as tts
import speech_recognition as sr
import commands as cmd

r = sr.Recognizer()
speaker = tts.init()
speaker.setProperty("rate", 150) # Speaking Speed ( words per minute )
speaker.setProperty('volume', 1.0) # Volume ( 0.0 to 1.0 )
# Change Voice
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def listenAndRecognize(text="Listening..."):
    print(text)
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)
    command = str(r.recognize_google(audio))
    command = command.lower()
    return command

def createNote():
    speak("What do you want to write onto your note?")
    note = listenAndRecognize()

    speak("Choose a filename!")
    filename = listenAndRecognize()

    with open(filename, 'w') as file:
        file.write(note)
        speak(f"I Successfully added the note to {filename}")
        
def quit():
    speaker.say("Thank You For Using Me!. Byee!")
    speaker.runAndWait()
    sys.exit(0)

def processCommand(c):
    c = str(c)
    # Open Any Link:
    if c.startswith("open"):
        site = c.split(" ")[1]
        link = cmd.open_cmds[site]
        wb.open(link)

    # Play Music from Library
    if c.startswith("play"):
        song = c.split(" ", 1)[1]
        link = cmd.music_library[song]
        wb.open(link)
    
    # Tells the Current Date and Time
    if ("time" in c) or ("current time" in c):
        current = dt.now() 
        dateTime = current.strftime("%B %d, %Y %H:%M") 
        speak("The Current Date and Time is " + dateTime)
        print(dateTime)
    
    # Make Notes
    if "make note" in c:
        createNote()
    
    # Exit the Program
    if ("quit" in c) or ("exit" in c):
        quit()

if __name__ == "__main__":

    while True:
        try:
            # Listen for the Wake Word
            message = listenAndRecognize()
            # Retrieve Wake Word from List
            index = cmd.wake_words.index(message)
            # wake_word = cmd.wake_words[index]

            if(index):
                response = random.choice(cmd.wake_responses)
                speak(response)

                while True:
                    try:
                        # Listen for Command
                        command = listenAndRecognize("Active...")
                        print(command)
                        processCommand(command)
                    except Exception as e:
                        print("Could not Understand. error".format(e))

        except sr.UnknownValueError:
            print("Could Not Understand")
        except Exception as e:
            print("Error".format(e))
            