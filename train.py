import speech_recognition as sr

r = sr.Recognizer()
while True:
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)
    command = r.recognize_google(audio)
    command = command.lower()

    print(command)

    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
        command = r.recognize_google(audio)
        command = command.lower()

        print(command)

    except sr.UnknownValueError:
        print("Could Not Understand")