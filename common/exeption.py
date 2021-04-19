import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 指向根目录文件夹 smslink
import traceback

def exeption(function):
    '''
    异常捕获
    :param function:
    :return:
    '''
    def catch(*args,**kwargs):
        try:
            return function(*args,**kwargs)
        except Exception:
            print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            et,ev,tb=sys.exc_info()
            # traceback.print_exception(et, ev, tb)
            msg=traceback.format_exception(et,ev,tb)
            for m in msg:
                print(m)

    return catch

if __name__=='__main__':
    pass

