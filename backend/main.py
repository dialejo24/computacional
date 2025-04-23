from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from qa_engine import load_pdf_vector_search, get_answer_from_pdf
from voz_texto import transcribe_audio
from texto_voz import text_to_speech
from voz_personalizada import audito_stream
from fastapi.middleware.cors import CORSMiddleware
import requests
import time
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/")
def read_root():
    print("hola")
    return {"message": "Hola mundo"}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    print("Recibiendo archivo PDF...")
    contents = await file.read()
    with open("uploaded.pdf", "wb") as f:
        f.write(contents)

    load_pdf_vector_search("uploaded.pdf")
    return {"message": "PDF cargado e indexado exitosamente."}

@app.post("/ask/")
async def ask_question(audio: UploadFile = File(...)):
    audio_path = "question.wav"    
    with open(audio_path, "wb") as f:
        f.write(await audio.read())

    question = transcribe_audio(audio_path)
    answer = get_answer_from_pdf(question)
    audio_file = ""

    try:
        audio_file = f"/{audito_stream(answer)}"
    except Exception as e:
        print(f"Error al reproducir el audio: {e}")

    if audio_file == "":
        audio_file = f"/audio/{text_to_speech(answer)}"
    response =  JSONResponse(content={
        "question": question,
        "answer": answer,
        "audio_path": audio_file
    })

    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.get("/audio/{filename}")
async def get_audio(filename: str):

    return FileResponse(f"audio/{filename}", media_type="audio/mpeg")