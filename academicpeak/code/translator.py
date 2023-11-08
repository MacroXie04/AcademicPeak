import requests
from academicpeak.code.Translate.AuthV3Util import addAuthParams
from langdetect import detect, DetectorFactory

APP_KEY = '3826d1e6c939ecaf'
APP_SECRET = 'lszlbHaIdLKlk6kTU31e9YNj57BcdxAM'


def translator(text):
    language_from, language_to = judge_language(text)
    if language_from == f'unknown':
        return "Error : Unknown UTF_8 Character"
    return generate_translation(text, language_from, language_to)


def judge_language(s: str) -> tuple[str, str] | str:
    if not s.strip():  # 如果字符串只包含空白或为空，则返回未知
        return 'unknown', 'unknown'

    try:
        detected_lang = detect(s)
        if detected_lang == 'zh-cn' or detected_lang == 'zh-tw':
            return 'zh-CHS', 'en'
        elif detected_lang == 'en':
            return 'en', 'zh-CHS'
        else:
            return 'unknown', 'unknown'
    except:
        return 'unknown', 'unknown'


def generate_translation(text, lang_from, lang_to):
    data = {'q': text, 'from': lang_from, 'to': lang_to}
    addAuthParams(APP_KEY, APP_SECRET, data)
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/api', header, data, 'post')
    return res.json()['translation'][0]


def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)
