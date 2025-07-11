🤖 Jarvis - Voice Controlled Assistant using Python

Jarvis is a voice-activated personal assistant built in Python. It can respond to your voice using wake-word detection, perform general tasks like playing music, reading the latest news, and opening websites — all without OpenAI integration.

---

## 🚀 Features

- 🎤 Wake word detection (`"Jarvis"`)
- 🗣️ Voice command processing
- 📢 Text-to-speech responses using `pyttsx3`
- 🌐 Opens popular websites like Google, Facebook, YouTube
- 📰 Reads top news headlines from India (via NewsAPI)
- 🎵 Plays songs by title using custom `musicLibrary.py` dictionary
- 🔍 YouTube search fallback for songs not in the library

---

## 🛠️ Technologies Used

- Python 3.x
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `requests`
- `difflib`
- NewsAPI

---

## 🗂️ Setup Instructions

1. Clone or download the project.
2. Install dependencies:

```bash
pip install speechrecognition pyttsx3 requests
```

3. Get a free NewsAPI key from [https://newsapi.org](https://newsapi.org) and add it to your code.
4. Create a `musicLibrary.py` file with your songs.

---

## 🎵 Example: `musicLibrary.py`

```python
music = {
    "bella ciao": "https://www.youtube.com/watch?v=0aUav1lx3rA",
    "mocking bird": "https://www.youtube.com/watch?v=S9bCLPwzSC0",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "sahiba": "https://www.youtube.com/watch?v=n2dVFdqMYGA"
}
```

---

## 👨‍💻 Author

- **Siddhant Kumar**
