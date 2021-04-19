import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import datetime


def linkparams():
    '''
    数据参数化---时间
    :return:
    '''
    end_min = (
        (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))  # 结束日期小于未大于当前时间1min
    end_year = (
        (datetime.datetime.now() + datetime.timedelta(days=367)).strftime("%Y-%m-%d %H:%M:%S"))  # 结束日期小于大于当前时间1year

    end_mins = ((datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S"))  # 符合创建时间

    assert_end_min = 32023
    assert_end_year = 32023

    # params_list = [(end_min, assert_end_min), (end_year, assert_end_year)]
    # params_list = [[end_min, assert_end_min], [end_year, assert_end_year], ['', 3001],[end_mins,200]]  # 存入列表中
    params_list = [[end_min, assert_end_min], [end_year, assert_end_year], ['', 3001]]  # 存入列表中

    # print(params_list)
    return params_list


def linknullvalue():
    '''
    传入空值
    :return:
    '''
    jsons = [[{}, 3001]]
    # print(jsons)
    return jsons


if __name__ == '__main__':
    # linkparams()
    linknullvalue()
