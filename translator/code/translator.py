import requests
import langid
from AuthV3Util import addAuthParams

class Translator:

    APP_KEY = '3826d1e6c939ecaf'
    APP_SECRET = 'lszlbHaIdLKlk6kTU31e9YNj57BcdxAM'

    @classmethod
    def translate(cls, text):
        """Translate text using Youdao API"""
        language_from, language_to = cls._judge_language(text)
        return cls._generate_translation(text, language_from, language_to)

    @classmethod
    def _judge_language(cls, s: str) -> tuple[str, str]:
        detected_language, _ = langid.classify(s)
        if detected_language == 'zh':
            return 'zh-CHS', 'en'
        elif detected_language == 'en':
            return 'en', 'zh-CHS'
        else:
            raise Exception("language does not support")


    @classmethod
    def _generate_translation(cls, text, lang_from, lang_to):
        data = {'q': text, 'from': lang_from, 'to': lang_to}
        addAuthParams(cls.APP_KEY, cls.APP_SECRET, data)
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = cls.do_call('https://openapi.youdao.com/api', header, data, 'post')
        result = res.json()['translation'][0]
        return {
            'original': text,
            'translation': result,
            'language': lang_from,
        }

    @classmethod
    def do_call(cls, url, header, params, method):
        if 'get' == method:
            return requests.get(url, params=params, headers=header)
        elif 'post' == method:
            return requests.post(url, data=params, headers=header)



if __name__ == '__main__':
    print(Translator.translate('你好'))
