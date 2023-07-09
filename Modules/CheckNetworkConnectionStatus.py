from Modules.staticINFO import *


def check_network_connection_status():
    url = "https://www.baidu.com/"
    try:
        if requests.get(url=url, headers=http_header, proxies=proxies).status_code == 200:
            return 0
    except requests.exceptions.ConnectionError:
        return -1
