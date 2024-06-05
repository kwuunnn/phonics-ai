#_*_encoding:utf-8_*_
import time
import hashlib
import requests
import json
import io
import soundfile as sf

"""
warnings:
- No valid audio detected!
- Audio volume too low!
- Audio volume too high!
- Audio not complete!
- Maybe not English audio!
"""

def speechsuper_word_score(audio_text, audio_bytes, content_type, appKey, secretKey):
    
    refText = audio_text
    audioType = content_type
    file_object = io.BytesIO(audio_bytes)
    audioSampleRate = sf.read(file_object)[1]

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

    params={
	    "connect":{
		    "cmd":"connect",
		    "param":{
			    "sdk":{
				    "version":16777472,
				    "source":9,
				    "protocol":2
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
    res=requests.post(url, data=data, headers=headers, files={"audio":audio_bytes})
    res_json = res.json()
    print(f"word_scores: {res_json['result']['words']}")
    print(f"pronunciation_scores: {res_json['result']['pronunciation']}")
    print(f"warning_message: {res_json['result']['warning']}")
    print(f"Audio sample rate: {audioSampleRate}")
    #return res.text.encode('utf-8', 'ignore').decode('utf-8')