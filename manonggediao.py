# coding:utf-8
from flask import Flask, request, make_response
from hashlib import sha1
from tokenManager import getToken
# from XMLHandler import parseRes, toxml
from dataHandler import data_handler
from logger import log
TOKEN = r'8Murt0xLt1wfb6f2fTLvM2xonrgjup92'

app = Flask(__name__)


@app.route('/wechat', methods=['GET'])
def check():
    token = TOKEN
    signature = request.args.get('signature', '')
    echostr = request.args.get('echostr', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    tmp = [timestamp, nonce, token]
    tmp.sort()
    tmp = ''.join(tmp)
    if signature == sha1(tmp.encode('utf-8')).hexdigest():
        return make_response(echostr)
    else:
        return "Access denied."


@app.route('/wechat', methods=['POST'])
def receive():
    try:
        return data_handler(request.data)
    except Exception as e:
        log(e)
        return ''
