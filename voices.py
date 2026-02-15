import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()

# for voice in voices:
#     print(voice, voice.id)
#     if 'pitch' in voice.__dict__:
#         print(f"{voice.id} supports pitch")