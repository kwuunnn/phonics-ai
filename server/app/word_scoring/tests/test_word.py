import requests

test_word = 'Apple'
test_audio_file = {'file' : open("./test_audio.wav", "rb")}

root = "http://127.0.0.1:8000/word/"

# word scoring
word_score = requests.get(root + f"pronunciation_score/{test_word}", files=test_audio_file)
print(word_score)