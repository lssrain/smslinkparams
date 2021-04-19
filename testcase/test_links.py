import json
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink

from common.batchno import *
from common.loggers import *
from paramdata.linkparams import *
from action.linkres import *
from common.exeption import *
import pytest, json
import allure

# header = header()
# loginfo = Log()
linkparams = linkparams()
linknullvalue = linknullvalue()


@allure.epic('天虹scrm')
@allure.feature('短信-小程序超链')
class TestLink:
    '''
    类名需含Test
    '''

    @allure.title('短信生成小程序超链测试用例')
    @pytest.mark.parametrize(['linktime', 'linkassert'],
                             linkparams)  # 引用参数化数据 根据参数化写入元组('linktime','linkassert')，或列表['linktime','linkassert']
    def test_addshort_date(self, linktime, linkassert):
        '''
        创建超链
        :return:
        '''
        print(linktime, linkassert)
        res = linkres(linktime, method='post', type='json')
        assert res.json()['code'] == linkassert

    @allure.title('短信生成小程序超链测试用例')
    @pytest.mark.parametrize(['linkjson', 'linkassert'],
                             linknullvalue)  # 引用参数化数据 根据参数化写入元组('linktime','linkassert')，或列表['linktime','linkassert']
    def test_addshort_nulldate(self, linkjson, linkassert):
        '''
        创建超链   是否永久有效不能为空\n链接类型code不能为空\n到期失效时间不能为空\n
        :return:
        '''
        print(linkjson, linkassert)
        res = linkresnull(linkjson, method='post', type='json')
        assert res.json()['code'] == linkassert


if __name__ == '__main__':
    # addshort_year()
    pytest.main(['-s', '-q', '--alluredir', './result'])
    os.system(r"allure generate --clean ./result -o ./result/report")
