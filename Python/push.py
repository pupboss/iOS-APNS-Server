#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apnsclient import *
import db

# 从数据库得到 Token
array = db.getNewestToken()

# 测试用 Token
testArr = ['5a15ef81cfa4b9dd11a448b6e8f7620d09475711dcd754be87d61a581c94189d','5a15ef81cfa4b9dd11a448b6e8f7620d09475711dcd754be87d61a581c94189d']

# 可以使用Session对象来维持连接池
session = Session()
con = session.get_connection("push_production", cert_file="cert.pem")

# 发送推送和得到反馈
message = Message(array, alert="新版已经发布啦~觉得好用可以分享~", badge=1)

# Send the message.
srv = APNs(con)
res = srv.send(message)

# Check failures. Check codes in APNs reference docs.
for token, reason in res.failed.items():
    code, errmsg = reason
    print "Device faled: {0}, reason: {1}".format(token, errmsg)

# Check failures not related to devices.
for code, errmsg in res.errors:
    print "Error: ", errmsg