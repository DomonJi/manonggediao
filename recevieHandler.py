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
            links = result['playlinks']
            return {
                'title': result['title'],
                'desc':  result['area'] + ' ' + result['tag'] + '\r\n' + result['act'] +
                '\r\n年份:' + result['year'] + '  评分:' + str(result['rating']) + '\r\n导演:' +
                result['dir'] + '\r\n' + result['desc'],
                'pic': result['cover'],
                'url': links.popitem()[1] if links and links.popitem()[1] else
                'http://m.iqiyi.com/search.html?key=' + query
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
