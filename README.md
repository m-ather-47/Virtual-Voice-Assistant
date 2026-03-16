# Virtual Voice Assistant

A Python-based virtual voice assistant that listens for wake words and responds to spoken commands. It uses Google Speech Recognition for voice input and pyttsx3 for text-to-speech output.

## Features

- **Wake Word Activation** — Listens continuously and activates on configurable wake words (e.g., "hey siri", "hello")
- **Open Websites** — Open predefined websites (Google, Facebook, YouTube, LinkedIn) by voice
- **Play Music** — Play songs from a built-in music library via YouTube
- **Tell Time** — Get the current date and time spoken aloud
- **Make Notes** — Dictate and save notes to text files
- **Customizable** — Easily add new commands, websites, and songs through `commands.py`

## Project Structure

```
virtual-voice-assistant/
├── main.py          # Entry point — core assistant loop
├── commands.py      # Wake words, URLs, and music library config
├── train.py         # Standalone script to test speech recognition
├── voices.py        # Utility to list and preview available TTS voices
└── .gitignore
```

## Prerequisites

- Python 3
- A working microphone
- An internet connection (required for Google Speech Recognition)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/m-ather-47/virtual-voice-assistant.git
   cd virtual-voice-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install SpeechRecognition pyttsx3 pyaudio
   ```
   > **Note:** On some systems, `pyaudio` requires [PortAudio](http://www.portaudio.com/) to be installed separately.

## Usage

**Run the assistant:**
```bash
python main.py
```

Say one of the wake words to activate, then speak a command:

| Command | Action |
|---|---|
| `"open google"` | Opens Google in your browser |
| `"open youtube"` | Opens YouTube in your browser |
| `"play [song name]"` | Plays a song from the music library |
| `"time"` / `"current time"` | Tells you the current date and time |
| `"make note"` | Dictates and saves a note to a file |
| `"quit"` / `"exit"` | Exits the assistant |

**Utility scripts:**
```bash
python voices.py   # List and preview available TTS voices
python train.py    # Test that your microphone and speech recognition work
```

## Configuration

Edit `commands.py` to customize:

- **`wake_words`** — Words that activate the assistant
- **`open_cmds`** — Websites the assistant can open
- **`music_library`** — Songs mapped to YouTube URLs

TTS voice, speed, and volume can be adjusted at the top of `main.py`.

## License

This project is open source and available under the [MIT License](LICENSE).
