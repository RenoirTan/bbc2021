import pyttsx3 as tts

def ex1():
    engine: tts.Engine = tts.init()
    engine.setProperty("rate", 100)
    # Feature suggestion: Add voice actors (especially James May)
    engine.say("oh cock")
    engine.runAndWait()
    print("Engine's speech rate: {0}wpm".format(engine.getProperty("rate")))


if __name__ == "__main__":
    ex1()
