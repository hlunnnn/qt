import time
import unittest
from parameterized import parameterized
import page
from base.getdriver import GetDriver
from page.page_login import PageLogin
from base.get_logger import GetLogger
from common.read_file import get_txt_data

log = GetLogger().get_logger()
get_data = get_txt_data("account.txt")


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        cls.login=PageLogin(cls.driver)

    def setUp(self):
        self.driver.get(page.index_url)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()
        # pass
    @parameterized.expand(get_data)
    @unittest.skip
    def test_1_register(self,username,pswd):
        try:
            self.login.email_register(username,pswd)
            time.sleep(2)
            self.assertEqual(True,self.login.islogin())
            # self.login.logout()
        except Exception as e:
            log.error("错误:{}".format(e))
            self.login.base_get_image()
            raise e


    @parameterized.expand(get_data)
    def test_2_login(self,username,pswd):
        try:
            self.login.email_login(username,pswd)
            self.assertEqual(True,self.login.islogin())
            self.login.logout()
        except Exception as e:
            log.error("错误:{}".format(e))
            self.login.base_get_image()

            raise e


if __name__ == '__main__':
    unittest.main()
