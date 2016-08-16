#coding:utf-8
from flask import Flask, g, request,make_response
import time
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug=True

@app.route('/', methods=['GET'])
def weixin_verify():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    token = 'jixiaomeng' #和申请消息接口时的Token一致
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = ''.join(tmplist)
    hashstr = hashlib.sha1(tmpstr).hexdigest()

    if hashstr == signature:
        return make_response(echostr) #success
    return 'access verification fail' #fail

if __name__=='__main__':
    app.run()
