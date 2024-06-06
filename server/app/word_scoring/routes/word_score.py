import os
from dotenv import load_dotenv
from fastapi import APIRouter, File, UploadFile
from word_scoring.models.api_speechsuper import *
from word_scoring.models.api_dolby import *

load_dotenv()

SS_appKey = os.getenv("SPEECHSUPER_APP_KEY")
SS_secretKey = os.getenv("SPEECHSUPER_SECRET_KEY")
DLB_appKey = os.getenv("DOLBY_APP_KEY")
DLB_secretKey = os.getenv("DOLBY_SECRET_KEY")
DLB_payload = { 'grant_type': 'client_credentials', 'expires_in': 1800 }
DLB_response = requests.post('https://api.dolby.io/v1/auth/token',
                        data=DLB_payload, auth=requests.auth.HTTPBasicAuth(DLB_appKey, DLB_secretKey))
DLB_body = json.loads(DLB_response.content)
DLB_api_token = DLB_body['access_token']

router = APIRouter()

# SpeechSuperAPI (until 19 June)
@router.get("/score/{word}")
async def word_score(word, file: UploadFile = File(...)):

    # read the original audio file as 'bytes' object
    og_audio_bytes = file.file.read()
    audio_type = file.filename.split('.')[1]
    # enhance audio quality
    enhanced_audio_bytes = dolby_enhance_audio(DLB_api_token, og_audio_bytes)
    # retrieve pronunciation scores
    scores = speechsuper_word_score(SS_appKey, SS_secretKey,
                                    audio_text=word, audio_bytes=enhanced_audio_bytes, audio_type=audio_type)
    return scores
