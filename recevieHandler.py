import httplib2
import json
from logger import log

SIMSIMIKEY = 'bb53d7be-fce1-4315-b7da-46c8890b621f'

http = httplib2.Http()


def processs(obj):
    def simsimi(text, lc='zh'):
        res_url = 'http://sandbox.api.simsimi.com/request.p?ft=1.0&key='
        try:
            response, content = http.request(
                res_url + SIMSIMIKEY + '&text=' + text + '&lc=' + lc)
            result = json.loads(content.decode())
            return result['response']
        except Exception as e:
            log(e)
            return '我无法回答'

    return simsimi(obj['Content'])
