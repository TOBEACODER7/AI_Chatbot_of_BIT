from aip import AipSpeech
import pyttsx3
import os

"""新建一个ApiSpeech，输入你自己的token"""
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

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
