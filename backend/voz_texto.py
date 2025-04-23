import whisper
import os

ffmpeg_path = r"D:\Usuario\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe" #defina la ruta en donde tenga definido el instalador de ffmpeg
os.environ["PATH"] += os.pathsep + r"D:\Usuario\Downloads\ffmpeg-7.1.1-full_build\ffmpeg-7.1.1-full_build\bin"

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
