#coding:utf-8
from flask import Flask, request, make_response
from hashlib import sha1

def create_app(config=None):

    app = Flask(__name__)
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
        token = r'jixiaomeng' # 这个根据自己的设置自行修改
        signature = request.args.get('signature', '')
        echostr = request.args.get('echostr', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        tmp = [timestamp, nonce, token]
        tmp.sort()
        tmp = ''.join(tmp)
        if signature == sha1(tmp).hexdigest():
            return  make_response(echostr)
        else:
            return "Access denied."
