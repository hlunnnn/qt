import time
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover("./",
                                                pattern='test*.py',
                                                top_level_dir=None)

    filepath = "../report/{}.html".format(time.strftime('%Y-%m-%d %H_%M_%S'))

    #定义测试报告的标题和描述
    # with open(filepath,'wb') as fp:
    #     HTMLTestRunner(stream=fp,title='云培训项目自动化测试报告',description='操作系统：win10  谷歌浏览器').run(suite)

    runner  = unittest.TextTestRunner()
    runner.run(suite)

