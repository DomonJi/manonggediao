#coding:utf-8
from flask import Flask, request, make_response
from hashlib import sha1
from tokenManager import getToken
from XMLHandler import parseRes,toxml
from logger import log

app = Flask(__name__)
log('123')

@app.route('/')
def index():
    return "Hello,World!"


@app.route('/wechat',  methods=['GET'])
def check():
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

@app.route('/wechat',methods=['POST'])
def receive():
    dic = parseRes(request.data)
    log(dic)
    try:
        send_xml = toxml(usrid=dic['FromUserName'],type='text',content=dic['Content'],from_usr_name=dic['ToUserName'])
        log(send_xml)
        return send_xml
    except Exception as e:
        log(e)
        log('failed')
        return ''
