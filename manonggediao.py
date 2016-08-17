#coding:utf-8
from flask import Flask, request, make_response
from hashlib import sha1

app = Flask(__name__)
def create_app(config=None):

    if config is not None:
        app.config.from_pyfile(config)
    # configure your app...
    return app


@app.route('/')
def index():
    return "Hello,World!"


@app.route('/wechat',  methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        token = r'8Murt0xLt1wfb6f2fTLvM2xonrgjup92' # 这个根据自己的设置自行修改
        signature = request.args.get('signature', '')
        echostr = request.args.get('echostr', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        tmp = [timestamp, nonce, token]
        tmp.sort()
        tmp = ''.join(tmp)
        if signature == sha1(tmp.encode('utf-8')).hexdigest():
            return  make_response(echostr)
        else:
            return "Access denied."
