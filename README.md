# 四川大学校园网(SCUNET)认证助手

四川大学校园网(SCUNET)认证助手，实现四川大学校园网（锐捷ePortal Web 认证）自动登录和用户信息获取。Sichuan University Campus Network (SCUNET) Authentication Assistant, which realizes automatic login and user information acquisition for Sichuan University Campus Network (Ruijie ePortal Web Authentication).

**本程序是一款独立软件，不依赖浏览器，可跨平台运行**



## 功能演示

### ![function.png](https://github.com/evin546/SCUNETAssistant/blob/main/img/function.png?raw=true)





## Windows平台小白用户请点击[这里](https://github.com/evin546/SCUNETAssistant/releases/)下载`SCUNETAssistant.zip`文件，修改配置文件后即可直接使用





## 环境支持
`python <= 3.9`

`Windows/Linux/Macos..`


## 安装
### 安装命令
#### 克隆本项目

`git clone https://github.com/evin546/SCUNETAssistant.git`

#### 安装依赖

`pip install requests`



## 修改配置文件

`config.ini`

```ini
[ACCOUNT]
# 校园网账号
user_id = xxxxx	
# 校园网密码
password = xxxxx		

[SERVICE]
# 可选 CHINATELECOM/CHINAUNICOM/CHINAMOBILE/EDUNET
service = CHINATELECOM

[ATTEMPT]
# 内网通讯异常时，允许的最大重试次数
max_attempts_allowed = 3
```



## 运行

`python SCUNETAssistant.py`
或点击 `Startup.bat`

### 设置开机启动（Windows）

创建`Startup.bat`的快捷方式，按下`Win+R`键，输入`shell:startup` 并回车，将快捷方式移动到打开的文件夹下



## 声明

### 使用本工具，即代表您已经充分理解并同意下列所有条款：

#### 数据收集和使用

 本工具收集的所有用户信息均由用户自行输入，通过配置文件读取，仅作为校园网认证凭据使用，作者不对任何形式的数据泄露承担责任

#### 责任免除

本程序不支持绕过校园网用户认证，不提供任何违背《四川大学学生守则》及相关法律法规的功能，作者不对任何因使用本程序导致的后果承担责任
