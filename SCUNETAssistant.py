from Modules.staticINFO import version
from Modules.AutoLogin import autologin
from Modules.ShowUserInfo import show_user_info
from Modules.Exit import app_exit
import time
import os

# 玄学代码 防止打包成exe后字符乱码
os.system("")
try:
    print("SCUNETAssistant\tVer:{}".format(version))
    print("本项目开源地址：https://github.com/evin546/SCUNETAssistant")

    user_index = autologin()

    while True:
        if user_index == -1:
            app_exit(5)
        else:
            time.sleep(1)
            show_user_info(user_index)
            app_exit(3)
except KeyboardInterrupt:
    print('\n\033[1;93m' + '[用户操作退出]' + '\033[0m')
