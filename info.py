#/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
import json
import time
from mail import mail_sender

url = 'http://api.f2pool.com/zec/YOUR KEY'
recevers = ['mail@addr.com']
title = '矿机消息'
def minerinfo():
    done = requests.get(url)
    scode = done.status_code
    if scode == 200 :
        minfo = json.loads(done.text)
        s1 = '当前矿机工作正常，当前算力为' + str(minfo['workers'][0][1]) + '，当前余额为' + str(round(minfo['balance'],4))
        s2 = '当前矿机工作异常，请及时处理'
        if minfo['worker_length_online'] >= 1 :
            mail_sender(s1,recevers,title)
        else :
            mail_sender(s2,recevers,title)
    else :
        minerinfo()

minerinfo()

