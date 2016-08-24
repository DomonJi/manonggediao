import httplib2
import urllib
import json
from logger import log
from config import ROBOTKEY, FILMSKEY
import re

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
                'url': result['playlinks'].popitem()[1]
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
            result = result['result']
            if 'url' in result:
                return {
                    'title': result['text'],
                    'url': result['url']
                }, 'qunar'
            return result['text'], 'text'
        except Exception as e:
            log(e)
            return '我无法回答', 'text'
    if re.match(r'^[?？]', parsed['Content']):
        return films(re.sub(r'^[?？]', '', parsed['Content']).strip())
    return answer(parsed['Content'])
