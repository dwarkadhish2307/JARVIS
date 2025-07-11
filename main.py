import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import difflib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()  # Do this only once
newsapi = "ec7b4e3c5bc74dd7aa3c53ce7f77d870"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1].strip()

        # Case-insensitive exact match
        link = next((url for title, url in musicLibrary.music.items() if title.lower() == song.lower()), None)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            # Try to find a close match (e.g., "mockingbord" instead of "mocking bird")
            available_songs = list(musicLibrary.music.keys())
            closest_match = difflib.get_close_matches(song, available_songs, n=1, cutoff=0.6)

            if closest_match:
                corrected = closest_match[0]
                speak(f"Did you mean {corrected}? Playing it now.")
                webbrowser.open(musicLibrary.music[corrected])
            else:
                # Search YouTube as fallback
                speak("Song not in library. Searching YouTube...")
                query = song.replace(" ", "+")
                youtube_url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(youtube_url)


    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=" + newsapi)
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if not articles:
                speak("Sorry, I couldn't find any news.")
            else:
                speak("Here are the top headlines.")
                for article in articles[:5]:
                    title = article.get("title")
                    if title:
                        speak(title)
                        
    elif "exit" in c.lower() or "thank you" in c.lower():
        speak("Goodbye!")
        return True

    return False


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio)
                print("You said:", wake_word)

                if "jarvis" in wake_word.lower():
                    speak("Ya")
                    
                    with sr.Microphone() as source:
                        print("Jarvis Active. Listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                        command = recognizer.recognize_google(audio)
                        print("Command received:", command)

                        should_exit = processCommand(command)
                        if should_exit:
                            break

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("Sorry, I didn't catch that. Please repeat.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("Error:", str(e))


