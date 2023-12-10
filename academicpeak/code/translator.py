import requests
from langdetect import detect
from academicpeak.code.Translate.AuthV3Util import addAuthParams
APP_KEY = '3826d1e6c939ecaf'
APP_SECRET = 'lszlbHaIdLKlk6kTU31e9YNj57BcdxAM'

def translator(text):
    """Translate text using Youdao API"""
    # Determine the source and target languages for translation.
    language_from, language_to = judge_language(text)
    # Return an error message if the language cannot be determined.
    if language_from == 'unknown':
        return "Error: Unknown UTF_8 Character"
    # Generate the translation using the identified languages.
    return generate_translation(text, language_from, language_to)


def judge_language(s: str) -> tuple[str, str] | str:
    """ Check if the string is empty or only contains whitespace; return 'unknown' if true."""
    if not s.strip():
        return 'unknown', 'unknown'

    try:
        # Detect the language of the input string.
        detected_lang = detect(s)
        # Return corresponding language codes for Chinese to English or English to Chinese translation.
        if detected_lang == 'zh-cn' or detected_lang == 'zh-tw':
            return 'zh-CHS', 'en'
        elif detected_lang == 'en':
            return 'en', 'zh-CHS'
        else:
            # Return 'unknown' for languages other than Chinese and English.
            return 'unknown', 'unknown'
    except:
        # Return 'unknown' in case of any exceptions during language detection.
        return 'unknown', 'unknown'


def generate_translation(text, lang_from, lang_to):
    # Prepare the data for the translation API request.
    data = {'q': text, 'from': lang_from, 'to': lang_to}
    # Add authentication parameters to the request data.
    addAuthParams(APP_KEY, APP_SECRET, data)
    # Set the header for the HTTP request.
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # Make the API call and return the translation result.
    res = doCall('https://openapi.youdao.com/api', header, data, 'post')
    return res.json()['translation'][0]


def doCall(url, header, params, method):
    # Make an HTTP GET or POST request based on the specified method.
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)
