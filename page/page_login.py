import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import page
from base.base import Base

from base.get_logger import GetLogger
from tool.read_file import get_txt_data

log = GetLogger().get_logger()

username = get_txt_data("account.txt")[0][0]
pswd = get_txt_data("account.txt")[0][1]




class PageLogin(Base):


    # 邮箱登录
    def email_login(self,username,pswd):
        log.info("[page_Login] 通过邮箱登录:账号:{} 密码:{}".format(username, pswd))
        #点击登录
        self.base_click((By.XPATH,"//span[text()='登录']"))
        time.sleep(1)
        #点击邮箱登录
        self.base_click((By.XPATH,"//div[@class='wx-scan-login']/*[name()='svg']"))
        #输入账号
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入邮箱']"),username)
        #输入密码
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入密码']"),pswd)
        #输入验证码
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入验证码']"),'9999')
        #点击登录
        self.base_click((By.XPATH,"//button[text()='登录']"))

    # 邮箱登录
    def email_login_success(self,username=username,pswd=pswd):
        log.info("[page_Login] 通过邮箱登录:账号:{} 密码:{}".format(username, pswd))
        #点击登录
        self.base_click((By.XPATH,"//span[text()='登录']"))
        time.sleep(1)
        #点击邮箱登录
        self.base_click((By.XPATH,"//div[@class='wx-scan-login']/*[name()='svg']"))
        #输入账号
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入邮箱']"),username)
        #输入密码
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入密码']"),pswd)
        #输入验证码
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入验证码']"),'9999')
        #点击登录
        self.base_click((By.XPATH,"//button[text()='登录']"))








    #判断是否登录
    def islogin(self):
        log.info("[page_Login] 判断是否登录成功")
        if self.base_element_isexist((By.CLASS_NAME,"user-box")):
            return True
        else:
            return False

    #邮箱注册
    def email_register(self,username,pswd):
        log.info("[page_Login] 通过邮箱注册:账号:{} 密码:{}".format(username, pswd))
        #点击注册
        self.base_click((By.CLASS_NAME, "reg-btn"))
        time.sleep(1)
        #点击邮箱注册
        self.base_click((By.XPATH, "//div[@class='wx-scan-login']/*[name()='svg']"))
        #输入账号
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入邮箱']"),username)
        #输入密码
        self.base_sendkeys((By.XPATH,"//input[@type='password']"),pswd)
        #输入验证码
        self.base_sendkeys((By.XPATH,"//input[@placeholder='请输入激活码']"),'9999')
        #勾选协议
        self.base_click((By.ID,"register_agreePrivacy"))
        #点击注册
        self.base_click((By.XPATH,"//button[@type='submit']"))

    #关闭弹窗
    def closemodal(self):
        log.info("[page_Login] 退出登录")
        self.base_click((By.XPATH,"//button[@class='ant-modal-close']"))

    #退出登录
    def logout(self):
        self.base_click((By.CLASS_NAME,"logout-btn"))


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(page.index_url)
    driver.maximize_window()
    login = PageLogin(driver)
    login.email_register("a123@dayee.com","a1234567")



