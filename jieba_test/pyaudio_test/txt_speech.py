from aip import AipSpeech
import pyttsx3
import os

"""新建一个ApiSpeech"""
APP_ID = '25477358'
API_KEY = 'qwVMmf9y9NYpNcDfeK2utwS3'
SECRET_KEY = 'Aw8wYs5M4hzNqGix4Rc3Hvv6Do11WIXq'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)


def speaker(text):
    result = client.synthesis(text,'zh',1,{
            'vol':5,
            'spd':1,
            'piy':7,
            'per':4,
        })
    if not isinstance(result,dict):
        with open('result.mp3','wb') as f:
            f.write(result)
    engine = pyttsx3.init()
    engine.say 
    """ os.remove('result.mp3') """
