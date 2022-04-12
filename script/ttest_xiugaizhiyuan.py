import time
import unittest

from parameterized import parameterized

import page
from base.getdriver import GetDriver
from page.page_ats import PageATS
from page.page_login import PageLogin
from page.page_position_list import PagePositionList
from base.get_logger import GetLogger
from tool.read_file import get_txt_data

log = GetLogger().get_logger()

username = get_txt_data("account.txt")[0][0]
pswd = get_txt_data("account.txt")[0][1]

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        cls.driver.get(page.index_url)
        cls.social=PagePositionList(cls.driver)
        cls.login=PageLogin(cls.driver)
        cls.login.email_login("hluntest001@163.com","a1234567")
        cls.handle_qt=cls.social.base_get_handle()
        cls.ats=PageATS(cls.driver)
        cls.social.base_new_window()
        cls.social.base_switch_to_new_window()
        cls.ats.ats_login()
        cls.handle_ats=cls.social.base_get_handle()



    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()
        # pass

    @parameterized.expand([("测试职位0227（无站点）","简历02223")])
    #投递无站点、志愿选择的职位
    def test_toudi_1(self,posname,resumename):

        try:
            self.social.base_switch_to_window_by_handle(self.handle_qt)
            self.social.plist_to_social()
            self.social.plist_deliver_position(posname)
            self.social.base_switch_to_window_by_handle(self.handle_ats)
            self.assertTrue(self.ats.ats_ss_qkjl(resumename,posname))
        except Exception as e:
            log.error("错误:{}".format(e))
            self.login.base_get_image()
            raise e

    #投递站点职位
    @parameterized.expand([("测试职位0227（站点）")])
    def test_toudi_2(self,posname):
        try:
            self.social.base_switch_to_window_by_handle(self.handle_qt)
            self.social.plist_to_campus()
            self.social.plist_deliver_position_station(posname)
            self.social.base_switch_to_window_by_handle(self.handle_ats)

            self.assertTrue(self.ats.ats_zhandian())
        except Exception as e:
            log.error("错误:{}".format(e))
            self.login.base_get_image()
            raise e




if __name__ == '__main__':
    unittest.main()
