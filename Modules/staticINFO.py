import requests

version = "1.0"

session = requests.Session()

# 设置requests库请求时不使用代理，防止代理出错
proxies = {"http": None, "https": None}

http_header = {"Accept": "*/*",
               "Accept-Encoding": "gzip, deflate",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/114.0.0.0 Safari/537.36"
               }
main_url = "http://192.168.2.135/"

retry_time = 1
