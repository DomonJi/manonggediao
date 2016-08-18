import httplib2
import urllib
import json
from logger import log

http = httplib2.Http()


def simsimi(text,lc='zh'):
    try:
        response,content = http.request('http://sandbox.api.simsimi.com/request.p?key=bb53d7be-fce1-4315-b7da-46c8890b621f&text='+text+'&lc='+lc)
        result = json.loads(content.decode())
        return result['response']
    except Exception as e:
        log(e)
        return '我无法回答'
