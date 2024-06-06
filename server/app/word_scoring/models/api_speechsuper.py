#_*_encoding:utf-8_*_
import time
import hashlib
import requests
import json
import io
import librosa
import soundfile as sf

"""
warnings:
- No valid audio detected!
- Audio volume too low!
- Audio volume too high!
- Audio not complete!
- Maybe not English audio!
"""

def speechsuper_word_score(appKey, secretKey, audio_text, audio_bytes, audio_type):
    
	# Read original audio bytes
	og_file_obj = io.BytesIO(audio_bytes)
    
	# Resample audio file to 16000Hz
	y, sr = librosa.load(og_file_obj)
	y_resampled = librosa.resample(y, orig_sr=sr, target_sr=16000)
	output_file_obj = io.BytesIO()
	sf.write(output_file_obj, y_resampled, 16000, format='WAV')
	output_file_obj.seek(0)
    
	refText = audio_text
	audioType = audio_type
	audioSampleRate = 16000
	baseURL = "https://api.speechsuper.com/"
	# Change the coreType according to your needs (word.eval.promax for scripted word scoring)
	coreType = "word.eval.promax"
	url =  baseURL + coreType
	timestamp = str(int(time.time()))
	userId = "guest"
	connectStr = (appKey + timestamp + secretKey).encode("utf-8")
	connectSig = hashlib.sha1(connectStr).hexdigest()
	startStr = (appKey + timestamp + userId + secretKey).encode("utf-8")
	startSig = hashlib.sha1(startStr).hexdigest()
	
	params = {
			"connect":{
				"cmd":"connect",
				"param":{
					"sdk":{
						"version":16777472,
						"source":9,"protocol":2
					},
					"app":{
						"applicationId":appKey,
						"sig":connectSig,
						"timestamp":timestamp
					}
				}
			},
			"start":{
				"cmd":"start",
				"param":{
					"app":{
						"userId":userId,
						"applicationId":appKey,
						"timestamp":timestamp,
						"sig":startSig
					},
					"audio":{
						"audioType":audioType,
						"channel":1,
						"sampleBytes":2,
						"sampleRate":audioSampleRate
					},
					"request":{
						"coreType":coreType,
						"refText":refText,
						"tokenId":"tokenId"
					}
				}
			}
		}
	
	datas=json.dumps(params)
	data={'text':datas}
	headers={"Request-Index":"0"}
	res=requests.post(url, data=data, headers=headers, files={"audio":output_file_obj})
	res_json = res.json()
	if 'warning' not in res_json['result']:
		res_json['result']['warning'] = 'No warning message'
	toReturn = {}
	toReturn['word_scores'] = res_json['result']['words']
	toReturn['pronunciation_score'] = res_json['result']['pronunciation']
	toReturn['warning_message'] = res_json['result']['warning']
	return toReturn