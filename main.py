# -*- coding: UTF-8 -*-
import requests
import time
import json
import sys


def get_format_time(time_stamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))


start_time = time.time()
print('此次运行开始时间为 :', get_format_time(start_time))
# email 覆盖于此

# passwd 覆盖于此

# 开始尝试签到
file_path = sys.path[0] + r'/config.json'
with open(file_path, 'r') as f:
    config = json.load(f)

root_url = config['root_url']

try_times = config['try_times']

sleep_second = config['sleep_second']

print('成功载入配置文件')
for i in range(try_times):
    print('第', i + 1, '次尝试签到')
    try:
        session = requests.Session()
        # 登录
        print('正在登录...')
        login_url = f'{root_url}/auth/login'
        res = session.post(login_url,
                           data={
                               'email': email,
                               'passwd': passwd,
                               'code': ''
                           })
        print('\n\t', res.json(), '\n')
        # 签到
        print('正在签到...')
        chekin_url = f'{root_url}/user/checkin'
        res = session.post(chekin_url)
        print('\n\t', res.json(), '\n')
    except Exception as e:
        print(e)
        print('********  签到失败')
    else:
        print('********  签到成功')
    finally:
        try:
            session.close()
        except:
            pass
    print('休眠', sleep_second, '秒\n')
    time.sleep(sleep_second)

stop_time = time.time()
print('此次运行开始时间为 :', get_format_time(start_time))
print('此次运行结束时间为 :', get_format_time(stop_time))
print('此次运行总共耗时 :',
      time.strftime("%H:%M:%S", time.gmtime(stop_time - start_time)))
