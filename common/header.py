import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

from common.tokens import *

token = tokens()


def header():
    '''
    headers设置
    :return:
    '''
    headers = {
        'jt': token,
        'Content-Type': 'application/json;charset=UTF-8'
    }
    # print(headers)
    return headers


if __name__ == '__main__':
    # header()
    pass
