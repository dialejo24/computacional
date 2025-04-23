from gtts import gTTS
import os

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text=text, lang='es')
    path = f"audio/{filename}"
    os.makedirs("audio", exist_ok=True)
    tts.save(path)
    return filename
