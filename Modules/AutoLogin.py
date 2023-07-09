import configparser
import time

import Modules.staticINFO
from Modules.staticINFO import *
from Modules.Exit import app_exit
from Modules.CheckNetworkConnectionStatus import check_network_connection_status
from urllib.parse import urljoin


# return说明： -1：异常    user_index:正常
def autologin():
    # 加载配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    # 请求前判断当前网络连接状态
    if check_network_connection_status() == 0:
        print("\033[92m[无需登录]\033[0m 当前网络连接正常")
        app_exit(3)
    else:
        try:
            print("\033[93m[正在登录]\033[0m")
            # 给配置文件对应变量赋值
            userid = config.get("ACCOUNT", "user_id")
            password = config.get("ACCOUNT", "password")
            service_code = ""

            if config.get("SERVICE", "service") == "CHINATELECOM":
                service_code = "%E7%94%B5%E4%BF%A1%E5%87%BA%E5%8F%A3"
            elif config.get("SERVICE", "service") == "CHINAMOBILE":
                service_code = "%E7%A7%BB%E5%8A%A8%E5%87%BA%E5%8F%A3"
            elif config.get("SERVICE", "service") == "CHINAUNICOM":
                service_code = "%E8%81%94%E9%80%9A%E5%87%BA%E5%8F%A3"
            elif config.get("SERVICE", "service") == "EDUNET":
                service_code = "internet"

            # 获取重定向的最终地址
            redirect_list = session.get(url=main_url, headers=http_header, proxies=proxies).history
            redirect_host = redirect_list[len(redirect_list) - 1].headers["location"]

            # 从最终地址中解析出登录所需queryString参数
            redirect_host_response = session.get(url=redirect_host, headers=http_header,
                                                 proxies=proxies).content.decode()
            login_querystring = (
                redirect_host_response
                [redirect_host_response.find("/index.jsp?") + 11:redirect_host_response.find("'</script>")])

            # 登录接口
            login_post_url = urljoin(main_url, "/eportal/InterFace.do?method=login")
            login_post_data = {"userId": userid,
                               "password": password,
                               "service": service_code,
                               "queryString": login_querystring,
                               "operatorPwd": "",
                               "operatorUserId": "",
                               "validcode": "",
                               "passwordEncrypt": "false"}

            # 登录逻辑
            while True:
                login_post_response = session.post(url=login_post_url, data=login_post_data, headers=http_header,
                                                   proxies=proxies)
                login_status = login_post_response.text.encode('raw_unicode_escape').decode()
                if login_status.find('"result":"success"') != -1:
                    print("\033[92m[登录成功]\033[0m")
                    user_index = login_status[login_status.find("userIndex") + 12:login_status.find('","result"')]
                    return user_index
                else:
                    if login_status.find('"message"'):
                        response_message = login_status[
                                           login_status.find('"message"') + 11: login_status.find('","forwordurl"')]
                        print("\033[91m[登录失败]\033[0m {}".format(response_message))
                    else:
                        print("\033[91m[登录失败]\033[0m 未知错误")
                    return -1

        except (configparser.NoSectionError, configparser.NoOptionError):
            print("\r\033[91m[配置文件解析错误]\033[0m 请修改配置文件")
            return -1

        # 内网通讯异常重试逻辑
        except requests.exceptions.ConnectionError:
            # 给配置文件对应变量赋值
            max_attempts_allowed: int = int(config.get("ATTEMPT", "max_attempts_allowed"))
            retry_time1 = Modules.staticINFO.retry_time
            while retry_time1 <= max_attempts_allowed:
                countdown = 15
                while countdown >= 0:
                    print(
                        "\r\033[91m[内网通讯异常]\033[0m 向登录接口请求数据失败，请检查WLAN连接情况，程序将在 {} 秒后自动进行第 ({}/{}) 次重试".format(
                            countdown, retry_time1, max_attempts_allowed), end="")
                    time.sleep(1)
                    countdown = countdown - 1
                print("\r正在进行第({}/{})次重试".format(retry_time1, max_attempts_allowed))
                Modules.staticINFO.retry_time = retry_time1 + 1
                return autologin()
            print("\r\033[91m[已达到配置文件设定的最大重试次数]\033[0m")
            return -1
