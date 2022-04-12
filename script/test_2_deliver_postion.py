import time
import unittest
from unittest import skip

from parameterized import parameterized

import page
from base.getdriver import GetDriver
from page.page_ats import PageATS
from page.page_login import PageLogin
from page.page_position_list import PagePositionList
from base.get_logger import GetLogger
from tool.read_file import get_txt_data

log = GetLogger().get_logger()
email = get_txt_data("account.txt")[0][0]  # 简历中邮箱  取注册账号的邮箱


class TestDeliverPosition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        cls.driver.get(page.index_url)
        cls.social = PagePositionList(cls.driver)
        PageLogin(cls.driver).email_login_success()
        cls.handle_qt = cls.social.base_get_handle()
        cls.ats = PageATS(cls.driver)
        cls.social.base_new_window()
        cls.ats.ats_login()
        cls.handle_ats = cls.social.base_get_handle()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()
        # pass

    @parameterized.expand([("测试职位0227（无站点）", email)])
    # 投递无站点、志愿选择的职位
    def test_1_toudi(self, position_name, email):

        try:
            self.social.base_switch_to_window_by_handle(self.handle_qt)
            self.social.plist_deliver_position(position_name, "social")
            time.sleep(3)
            self.social.base_switch_to_window_by_handle(self.handle_ats)
            self.assertTrue(self.ats.ats_ss_qkjl(email, position_name))
        except Exception as e:
            log.error("错误:{}".format(e))
            self.social.base_get_image()
            raise e


    # 投递站点职位
    @parameterized.expand([("测试职位0227（站点）", email)])
    def test_2_toudi(self, position_name, email):
        try:
            self.social.base_switch_to_window_by_handle(self.handle_qt)
            self.social.plist_deliver_position_station(position_name, "social")
            time.sleep(3)
            self.social.base_switch_to_window_by_handle(self.handle_ats)
            self.assertTrue(self.ats.ats_zhandian(position_name,email))
        except Exception as e:
            log.error("错误:{}".format(e))
            self.social.base_get_image()
            raise e

    def test_3_search_1_pos_name(self):
        self.social.base_switch_to_window_by_handle(self.handle_qt)
        self.social.plist_to_social()
        self.assertTrue(self.social.plist_ss_pos_name("测试职位0227（无站点）"))

    def test_3_search_2_pos_locate(self):
        self.social.plist_to_social()
        self.assertTrue(self.social.plist_ss_pos_locate())

    def test_3_search_3_pos_cate(self):
        self.social.plist_to_social()
        self.assertTrue(self.social.plist_ss_pos_cate())

    def test_3_search_4_pos_company(self):
        self.social.plist_to_social()
        self.assertTrue(self.social.plist_ss_pos_company())
    def test_3_search_5_pos_salarys(self):
        self.social.plist_to_social()
        self.assertTrue(self.social.plist_ss_pos_salary())




if __name__ == '__main__':
    unittest.main()
