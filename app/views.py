from django.shortcuts import HttpResponse
import requests
import re
import time



def get_localhost_ip(request):
    response = requests.get("http://" + str(time.localtime().tm_year) + ".ip138.com/ic.asp")
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", response.content.decode(errors='ignore')).group(0)
    print(ip)
    return HttpResponse("localhost_ip : %s"%ip)


def get_request_ip(request):

    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    except:
        ip = None

    print(ip)

    return HttpResponse("request_ip : %s" % ip)