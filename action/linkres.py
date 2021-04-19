import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

import requests
import json
from common.header import *
from common.loggers import *
from common.exeption import *

headers = header()
loginfo = Log()

url = 'http://sit-hlj.rainbowcn.com/api/v1/scrm-message/uri/convert/miniapp/short'


def reqs(parames, method, type):
    global res
    loginfo.info("入参：{}".format(parames))
    if method.lower() == 'post'.lower():
        if type.lower() == 'json'.lower():
            res = requests.post(url, json=parames, headers=headers, verify=False)
        elif type.lower() == 'data'.lower():
            res = requests.post(url, data=parames, headers=headers, verify=False)

    elif method.lower() == 'get'.lower() :
        if type.lower() == 'json'.lower():
            res = requests.get(url, json=parames, headers=headers, verify=False)
        elif type.lower() == 'data'.lower():
            res = requests.get(url, data=parames, headers=headers, verify=False)

    loginfo.info("出参：{}".format(json.dumps(res.json(), sort_keys=True, ensure_ascii=False)))
    return res


def linkres(linktime, method,type):
    parames = {
        "linkTypeCode": "fixed",
        "miniAppId": 66,
        "params": {
            "linkBackType": 1,
            "code": "fixed",
            "pageCode": "shopIndex",
            "pageId": 1,
            "pageName": "购物首页",
            "pagePath": "index/pages/shopping/shopping",
            "typeCode": "shopIndex"
        },
        "paramsJsonString": str(
            {"linkBackType": 1, "code": "fixed", "pageCode": "shopIndex", "pageId": 1, "pageName": "购物首页",
             "pagePath": "index/pages/shopping/shopping", "typeCode": "shopIndex"}),
        "isExpire": 0,
        "expireTime": linktime
    }
    return reqs(parames, method,type)


def linkresnull(linkjson, method,type):
    parames = linkjson
    return reqs(parames, method,type)


if __name__ == '__main__':
    pass
