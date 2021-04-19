import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pymysql
import datetime
import ast


def runsql():
    '''
    连接数据库获取参数
    :return:
    '''
    result = []  # 存放数据库数据
    results = []  # 元组数据存入列表
    db = pymysql.connect(host='192.168.197.81', port=3306, user='root', password='123456', db='mysql',
                         charset='utf8')
    cursor = db.cursor()

    cursor.execute("select sms_message from smslink;")

    end_min = (
        (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))  # 结束日期小于未大于当前时间1min
    end_year = (
        (datetime.datetime.now() + datetime.timedelta(days=367)).strftime("%Y-%m-%d %H:%M:%S"))  # 结束日期小于大于当前时间1year

    params_end = [end_min, end_year]
    for i in cursor.fetchall():
        result.append(i[0])

    for i in range(len(params_end)):
        results.append((params_end[i], result[i]))  # 存入元组中
        # results.append([params_end[i],result[i]]) #存入列表中
    print(results)

    return results


if __name__ == '__main__':
    runsql()
