[TOC]

# ip

## #0 Blog

```
https://blog.csdn.net/Coxhuang/article/details/86657819
```

## #1 环境

```
python3.6
Django==2.0.7
```

## #2 需求
- 获取本地ip
- 获取访问者ip

## #3 获取本地ip


```
from django.shortcuts import HttpResponse
import requests
import re
import time

def get_localhost_ip(request):
    response = requests.get("http://" + str(time.localtime().tm_year) + ".ip138.com/ic.asp")
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", response.content.decode(errors='ignore')).group(0)
    print(ip)
    return HttpResponse("localhost_ip : %s"%ip)
```

>>> localhost_ip : 61.145.167.223


## #4 获取访问者ip

settings.py

```
ALLOWED_HOSTS = ["*"]
```

views.py

```
def get_request_ip(request):

    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    except:
        ip = None

    return HttpResponse("request_ip : %s" % ip)
```

>>> request_ip : 127.0.0.1

### #4.1 注意

- 如果是本地访问本地的接口,那么ip就是本机ip,不是本机对应的外网ip(127.0.0.1)
- 如果是局域网访问,那么拿到的ip是局域网的ip,并不是局域网内PC对应的外网ip(192.168.x.xxx)
- 如果是外网访问接口,那么拿到的ip就是访问者外网的ip(外网)

