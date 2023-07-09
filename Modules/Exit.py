import time


def app_exit(delay_time):
    print("\033[93m[自动退出]\033[0m 程序即将自动退出")
    time.sleep(delay_time)
    exit()
