# encoding:utf-8
import requests

class Translation():
    def __init__(self,to='en'):
        self.to = to
    def translate(self,keyword):
        url = "https://cn.bing.com/ttranslatev3?&IG=F77C176768894422AAA70AFFA98CC78B&IID=SERP.5529.18"
        data = {
            "fromLang": "auto-detect",
            "text": f"{keyword}",
            "to": self.to
        }
        response = requests.post(url,data).json()
        print(response)
        detected = response[0]['detectedLanguage']['language']
        translated_text = response[0]['translations'][0]['text']
        to = response[0]['translations'][0]['to']
        print(f'''
        原文语言:{detected}
        目标语言:{to}
        翻译内容:{keyword}
        翻译结果:{translated_text}
        
        ''')
if __name__ == '__main__':
    t = Translation('zh-Hans')
    t.translate('china')