# Python Voice Assistant

A simple voice-controlled desktop assistant built in **Python** using the 'speech-recognition' library.
This assistant listens for your voice commands, responds in real time, and performs tasks such as opening websites, telling the time, and playing music.

## Features
- **Always listening** using background speech recognition
- **Tells the current time**
- **Opens popular websites** (Google, YouTube, Wikipedia)
- ** Plays music on YouTube**
- **Basic text responses** (can be upgraded to text-to-speech)
- **Stops on command** ("stop", "exit", or "goodbye")

## How It Works
1. The program uses the **Google Speech Recognition API** to convert your voice into text.
2. It continuously listens in the background using 'listen_in_background()' from the 'speech_recognition' module.
3. When it detects a command, it processes the text and performs the corresponding action, like opening a browser or printing a message.

## Requirements
Make sure you have **Python 3.8+** installed, then install these dependencies:

``` bash
pip install SpeechRecognition
pip install PyAudio
```

## Example Commands
- "What time is it?" = Tells the current time
- "Open Google" = Opens Google in browser
- "Open Wikipedia" = Opens Wikipedia main page
- "Open YouTube" = Open YouTube
- "Play music" = Opens a preset YouTube song
- "Stop"/"Exit"/"Goodbye" = Closes the program

## Project Structure
``` bash
voice-assistant/
│
├── assistant.py        # Main Python program
├── README.md           # Project documentation
└── requirements.txt    # Dependencies list

```

## Running the Program
1. Clone the Repository:
``` bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```
2. Install dependencies:
``` bash
pip install -r requirements.txt
```
3. Run the assistant:
``` bash
python assistant.py
```
