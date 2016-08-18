import xml.etree.ElementTree as ET
import json
import time

def parseRes(res):
    recv_xml = ET.fromstring(res)
    return {
        'ToUserName':recv_xml.find('ToUserName').text,
        'FromUserName':recv_xml.find('FromUserName').text,
        'CreateTime':recv_xml.find('CreateTime').text,
        'MsgType':recv_xml.find('MsgType').text,
        'Content':recv_xml.find('Content').text
    }

def toxml(usrid,type,**kwargs):
    return "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>" % (usrid,kwargs['from_usr_name'],str(int(time.time())),type,kwargs['content'])
