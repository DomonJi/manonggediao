import xml.etree.ElementTree as ET
from recevieHandler import processs
from logger import log
import time


def data_handler(data):
    recv_field_list = ['ToUserName', 'FromUserName',
                       'CreateTime', 'MsgType', 'Content']

    def parse_res(data):
        recv_xml = ET.fromstring(data)
        return {t: recv_xml.find(t).text for t in recv_field_list}

    parsed = parse_res(data)

    def toxml(processed, msgtype):
        def wrap(t, c):
            return '<' + t + '><![CDATA[' + c + ']]></' + t + '>'

        if msgtype == 'text':
            return '<xml>' + wrap('ToUserName', parsed['FromUserName']) +\
                wrap('FromUserName', parsed['ToUserName']) +\
                wrap('CreateTime', str(int(time.time()))) +\
                wrap('MsgType', 'Text') + wrap('Content', processed) + '</xml>'
        if msgtype == 'films':
            send = '<xml>' + wrap('ToUserName', parsed['FromUserName']) +\
                wrap('FromUserName', parsed['ToUserName']) +\
                wrap('CreateTime', str(int(time.time()))) +\
                wrap('MsgType', 'news') + wrap('ArticleCount', '1') + '<Articles><item>' +\
                wrap('Title', processed['title']) + wrap('Description', processed['desc']) + \
                wrap('PicUrl', processed['pic']) + wrap('Url', processed['url']) + \
                '</item></Articles>' + '</xml>'
            log(send)
            return send
        if msgtype == 'qunar':
            send = '<xml>' + wrap('ToUserName', parsed['FromUserName']) +\
                wrap('FromUserName', parsed['ToUserName']) +\
                wrap('CreateTime', str(int(time.time()))) +\
                wrap('MsgType', 'news') + wrap('ArticleCount', '1') + '<Articles><item>' +\
                wrap('Title', processed['title']) + wrap('Url', processed['url']) + \
                '</item></Articles>' + '</xml>'
            log(send)
            return send

    processed, msgtype = processs(parsed)
    return toxml(processed, msgtype)
