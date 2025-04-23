from elevenlabs.client import ElevenLabs
import time
import os

# Inicializa el cliente con tu API key
client = ElevenLabs(api_key="")

# Texto a convertir

# ID de la voz que quieres usar (puedes cambiarlo)
voice_id = "JBFqnCBsd6RMkjVDRZzb"  # Ejemplo: "Rachel", "Bella", etc.

# Obtiene el stream de audio

def audito_stream(text: str):

    audio_stream = client.text_to_speech.convert_as_stream(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2"
        
    )
    timestamp = int(time.time())
    folder = "audio"
    os.makedirs(folder, exist_ok=True)
    filename = "audio/output.mp3"

    with open(filename, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    print(f"✅ Audio guardado como {filename}")
    return filename
