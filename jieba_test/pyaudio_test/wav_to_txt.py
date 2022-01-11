from aip import AipSpeech

"""新建一个ApiSpeech"""
APP_ID = '25477358'
API_KEY = 'qwVMmf9y9NYpNcDfeK2utwS3'
SECRET_KEY = 'Aw8wYs5M4hzNqGix4Rc3Hvv6Do11WIXq'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def get_file_content(filePath):
   
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_text():
    result = client.asr(get_file_content('output.wav'), 'wav', 16000, {
    'dev_pid': 1536,})
    print(result)
    text = result['result'][0]
    return text



