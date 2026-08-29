import datetime
import os
import sys
import webbrowser

# Try importing audio libraries; fallback to text if they are unavailable
try:
    import pyttsx3
    import speech_recognition as sr

    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False


def speak(text):
    """Provides audio feedback if available, otherwise prints to console."""
    print(f"Assistant: {text}")
    if AUDIO_AVAILABLE:
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass  # Fallback gracefully if speech engine fails


def listen_command():
    """Captures voice input or falls back to text input."""
    if not AUDIO_AVAILABLE:
        return input("\nYou (Type your command): ").lower()

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("I didn't catch that. Could you please repeat it?")
            return ""
        except sr.RequestError:
            speak("Network error. Switching to text input.")
            return input("\nYou (Type your command): ").lower()
        except Exception:
            # Fallback if microphone access fails on tablet
            return input("\nYou (Type your command): ").lower()


def main():
    if not AUDIO_AVAILABLE:
        print(
            "⚠️ Audio libraries not fully configured on this device. Running in Text-Fallback Mode."
        )

    speak(
        "Voice Assistant initialized. Say hello, ask for the time, or search the web!"
    )

    while True:
        query = listen_command()

        if not query:
            continue

        # 1. Respond to Hello
        if "hello" in query or "hi" in query:
            speak("Hello! How can I help you today?")

        # 2. Tell the current time and date
        elif "time" in query or "date" in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            current_date = now.strftime("%B %d, %Y")
            speak(f"Today is {current_date} and the current time is {current_time}.")

        # 3. Perform a web search
        elif "search" in query:
            speak("What topic would you like me to search for?")
            search_topic = listen_command()
            if search_topic:
                speak(f"Searching web for {search_topic}...")
                url = f"https://google.com{search_topic}"
                webbrowser.open(url)

        # Exit Command
        elif "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye! Have a productive day.")
            break

        # 4. Graceful Error Handling for unsupported statements
        else:
            speak(
                "I am not programmed for that command yet. Please try saying hello, time, or search."
            )


if __name__ == "__main__":
    main()

