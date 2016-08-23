import httplib2
import urllib
import json
from logger import log
from config import ROBOTKEY, FILMSKEY

http = httplib2.Http()


def processs(parsed):
    def films(query):
        url = 'http://op.juhe.cn/onebox/movie/video?key='
        response, content = http.request(
            url + FILMSKEY + '&q=' + query)
        try:
            result = json.loads(content.decode())
            result = result['result']
            return {
                'title': result['title'],
                'desc': result['desc'],
                'pic': result['cover'],
                'link': result['playlinks'].popitem()[1]
            }, 'films'
        except Exception as e:
            log(e)
            return '无法查询到结果', 'text'

    def answer(text):
        url = 'http://op.juhe.cn/robot/index?key='
        response, content = http.request(
            url + ROBOTKEY + '&info=' + text + '&userid=' + parsed['FromUserName'])
        try:
            result = json.loads(content.decode())
            return result['result']['text'], 'text'
        except:
            return '我无法回答', 'text'

    if parsed['Content'].startswith('影视 '):
        return films(parsed['Content'].replace('影视 ', ''))
    return answer(parsed['Content'])
