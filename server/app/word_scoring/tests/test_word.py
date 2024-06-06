import requests

test_word = 'Apple'
test_audio_file = {'file' : open("./test_audio.wav", "rb")}

root = "http://127.0.0.1:8000/words/"

# word scoring
word_score = requests.get(root + f"score/{test_word}", files=test_audio_file)
word_score_json = word_score.json()
print(f"word_scores: {word_score_json['word_scores']}")
print(f"pronunciation_scores: {word_score_json['pronunciation_score']}")
print(f"warning_message: {word_score_json['warning_message']}")