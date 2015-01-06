##本地php推送服务器使用方法

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

这四个文件改成自己的，ck.pem换成自己的，具体的制作方法可以看我的博客 [iOS8的推送](http://blog.pupboss.com/2015/01/05/iOS8-APNS/)

分类id是iOS8的新特性，需要根据自己情况来设置，上面的博客中有介绍。
