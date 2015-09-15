# 本地 php 推送服务器使用方法

## PHP 版

```
// Put your device token here (without spaces):
// 放置你的 device token:
$deviceToken = '****';

// Put your private key's passphrase here:
// 放置你的私钥密码:
$passphrase = 'xxxx';

// Put your alert message here:
// 放置你的提示信息:
$message = '杰哥是天才！!';

// Put your category id here:
// 放置你的分类id:
$category = 'alert';
```
## Python 版支持批量推送

db.py:
数据库相关语句换成自己的

push.py:
```
测试用 Token 换成自己的
testArr = ['5a15ef81cfa4b9dd11a448b6e8f7620d09475711dcd754be87d61a581c94189d','5a15ef81cfa4b9dd11a448b6e8f7620d09475711dcd754be87d61a581c94189d']

沙盒环境和证书名称修改下
session = Session()
con = session.get_connection("push_production", cert_file="cert.pem")

推送内容和小角标修改下
message = Message(array, alert="新版已经发布啦~觉得好用可以分享~", badge=1)
```

这四个字段改成自己的，ck.pem 换成自己的，具体的制作方法可以看我的博客 [iOS8的推送](https://pupboss.com/ios8-apns/)

分类 id 是 iOS8 的新特性，需要根据自己情况来设置，上面的博客中有介绍。

### Run

`php simplepush.php`

`python push.py`
