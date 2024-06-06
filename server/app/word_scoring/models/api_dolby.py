import requests
import soundfile as sf
import io
import json

def dolby_enhance_audio(api_token, audio_bytes):
    
    headers = {
        "Authorization": "Bearer {0}".format(api_token),
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    ########## upload bytes from local to temp dolby storage ##########
    store_url = "https://api.dolby.com/media/input"
    store_body = {
        "url": "dlb://word_storage/input/test_audio.wav",
    }
    store_response = requests.post(store_url, json=store_body, headers=headers)
    store_response.raise_for_status()
    store_data = store_response.json()
    store_presigned_url = store_data["url"]
    requests.put(store_presigned_url, data=audio_bytes)

    ########## enhance audio file and save to temp dolby storage ##########
    enhance_url = "https://api.dolby.com/media/enhance"
    enhance_body = {
        "input" : "dlb://word_storage/input/test_audio.wav",
        "output" : "dlb://word_storage/output/test_audio.wav",
    }
    enhance_response = requests.post(enhance_url, json=enhance_body, headers=headers)
    enhance_response.raise_for_status()

    ########## download enhanced audio file from temp dolby storage ##########
    get_url = "https://api.dolby.com/media/output"
    get_body = {
        "url": "dlb://word_storage/output/test_audio.wav",
    }
    get_response = requests.post(get_url, json=get_body, headers=headers)
    get_response.raise_for_status()
    get_data = get_response.json()
    get_presigned_url = get_data["url"]
    response = requests.get(get_presigned_url)
    """
    # save to local directory (test)
    with open("../enhanced_test_audio.wav", "wb") as file:
        file.write(response.content)
    """
    return response.content