from aip import AipSpeech

"""新建一个ApiSpeech，输入你自己的token"""
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

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



