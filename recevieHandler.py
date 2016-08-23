import httplib2
import urllib
import json
from logger import log
from config import ROBOTKEY

http = httplib2.Http()


def processs(obj):
    def answer():
        url = 'http://op.juhe.cn/robot/index?key='
        response, content = http.request(
            url + ROBOTKEY + '&info=' + obj['Content'] + '&userid=' + obj['FromUserName'])
        try:
            result = json.loads(content.decode())
            return result['result']['text']
        except:
            return '我无法回答'
    return answer()
