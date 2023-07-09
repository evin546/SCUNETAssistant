import json
import time
from urllib.parse import urljoin
from Modules.staticINFO import *


def show_user_info(user_index):
    try:
        get_user_info_post_url = urljoin(main_url, "/eportal/InterFace.do?method=getOnlineUserInfo")
        get_user_info_post_data = {
            "userIndex": user_index
        }
        # 锐捷eportal后端：请求该接口可能返回信息不全，这里多次请求，获取完整信息
        count = 0
        while True:
            count = count + 1
            user_info = session.post(url=get_user_info_post_url, headers=http_header, data=get_user_info_post_data,
                                     proxies=proxies).text.encode('raw_unicode_escape').decode()
            if user_info.find('"result":"success"') != -1:
                break
            elif count == 5:
                print("\033[93m[获取用户信息失败]\033[0m")
            time.sleep(0.01)

        json_user_info = json.loads(user_info)
        user_id = json_user_info.get("userId")
        service_name = json_user_info.get("service")
        user_ip = json_user_info.get("userIp")
        if service_name != "校园网":
            remaining_available_time = "无限制"
        else:
            remaining_available_time = json_user_info.get("maxLeavingTime")

        print("\033[92m[用户信息]\033[0m")
        print("校园网账号:", user_id)
        print("当前服务:", service_name)
        print("内网IP:", user_ip)
        print("剩余可用时长：", remaining_available_time)
    except requests.exceptions.ConnectionError:
        print("\033[93m[获取用户信息失败]\033[0m 无法访问信息接口")
