# coding:'utf-8'
import httplib2
import urllib
import json
import time
from config import APPID, SECRET

http = httplib2.Http()
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&'


def encodeurl(url):
    return url + 'appid=' + APPID + '&secret=' + SECRET


def initToken():
    token = ''
    expires_in = 0
    acquired_time = None

    def getToken(refresh=False):
        nonlocal token, expires_in, acquired_time
        if token and time.time() - acquired_time < expires_in and not refresh:
            return token
        response, content = http.request(encodeurl(url))
        try:
            res = json.loads(content.decode())
            token = res['access_token']
            expires_in = res['expires_in']
            acquired_time = time.time()
            print(token)
        except Exception as e:
            print(e)
        return token
    return getToken

getToken = initToken()
