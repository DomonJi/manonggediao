import xml.etree.ElementTree as ET
from recevieHandler import processs
import time


def data_handler(data):
    recv_field_list = ['ToUserName', 'FromUserName',
                       'CreateTime', 'MsgType', 'Content']

    def parse_res(data):
        recv_xml = ET.fromstring(data)
        return {t: recv_xml.find(t).text for t in recv_field_list}

    parsed = parse_res(data)

    def toxml(processed):
        def wrap(t, c):
            return '<' + t + '><![CDATA[' + c + ']]></' + t + '>'

        return '<xml>' + wrap('ToUserName', parsed['FromUserName']) +\
            wrap('FromUserName', parsed['ToUserName']) +\
            wrap('CreateTime', str(int(time.time()))) +\
            wrap('MsgType', 'Text') + wrap('Content', processed) + '</xml>'

    return toxml(processs(parsed))
