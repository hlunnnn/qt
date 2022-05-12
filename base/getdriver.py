from selenium import webdriver

import page


class GetDriver:
    driver=None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
        return cls.driver


    #关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


