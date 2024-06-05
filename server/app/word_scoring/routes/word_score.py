import os
from dotenv import load_dotenv
from fastapi import APIRouter, File, UploadFile
from word_scoring.models.speechsuper_api import speechsuper_word_score

load_dotenv()

SS_appKey = os.getenv("SPEECHSUPER_APP_KEY")
SS_secretKey = os.getenv("SPEECHSUPER_SECRET_KEY")

router = APIRouter()

# SpeechSuperAPI (until 19 June)
@router.get("/pronunciation_score/{word}")
async def pronunciation_score(word, file: UploadFile = File(...)):

    audio_bytes = file.file.read() # read the file as 'bytes' object
    content_type = file.filename.split('.')[1]
    scores = speechsuper_word_score(word, audio_bytes, content_type, SS_appKey, SS_secretKey)
