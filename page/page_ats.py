import time

from selenium.webdriver.common.by import By

import page
from base.base import Base
from base.get_logger import GetLogger
from common.common import get_socail_excel_data, get_campus_excel_data, read_json
log = GetLogger().get_logger()

class PageATS(Base):


    def ats_log(self, url, code, username, password):
        self.driver.get(url)
        self.base_send_keys(page.login_code, code)
        self.base_sendkeys(page.login_username, username)
        self.base_sendkeys(page.login_password, password)
        self.base_click(page.login_button)

    def ats_login(self):
        login_data = read_json("login.json")
        self.ats_log(login_data["url"],
                   login_data["code"],
                   login_data["username"],
                   login_data["password"])


    #搜索全库简历，判断是否搜索到简历
    def ats_ss_qkjl(self,email,position_name):
        self.base_sendkeys((By.ID,"quickSearchCondition"),email)
        self.base_enter((By.ID,"quickSearchCondition"))
        # return self.base_element_isexist((By.XPATH,"//div[@class='wtspe-table-left']/div[2]//tbody/tr[1]/td[3]//span[1]")) #第一条简历
        flag=self.base_element_isexist((By.XPATH,"//span[@title='{}']".format(position_name)))
        self.ats_out_qkjl()
        return flag

    #候选人页面   判断应聘记录的站点
    #站点为--返回False   站点不为--返回True
    def ats_zhandian(self,position_name,email):
        self.base_click((By.XPATH,"//div[@data-title='快速入口']"))
        self.base_click((By.XPATH,"//span[@title='候选人']/.."))
        # flag=self.base_get_text((By.XPATH,"(//td[@propname='siteName'])[4]"))
        self.base_sendkeys((By.XPATH,".//input[@placeholder='搜索职位，支持拼音']"),position_name)
        self.base_click((By.XPATH,"//div[@id='canidate-left-position']//span[text()='{}']".format(position_name)))
        time.sleep(2)
        flag = self.base_get_text((By.XPATH, "//td[text()='{}']/../td[@propname='siteName']".format(email)))
        self.ats_out_hxr()
        if flag!="--":
            return True
        else:
            return False

    #全局简历界面操作删除
    def ats_out_qkjl(self):
        log.info("[page_ats] 执行删除简历")
        self.base_click((By.XPATH,"//i[@class='wtspeicon wtspeicon-more operation-more']"))
        self.base_click((By.XPATH,"//span[text()='查看/编辑']"))
        self.base_click((By.XPATH,"//li[text()='删除']"))
        self.base_click((By.XPATH,"//span[text()='是否要删除该应聘信息？']/../div/a[text()='确 定']"))

    #候选人界面操作删除简历
    def ats_out_hxr(self):
        log.info("[page_ats] 执行删除简历")
        self.base_click((By.XPATH,"//i[@class='wtspeicon wtspeicon-more operation-more wtspe-theme-word-hv']"))
        self.base_click((By.XPATH,"//span[text()='查看/编辑']"))
        time.sleep(1)
        log.info("[page_ats] 准备删除简历")
        self.base_click((By.XPATH,"//li[text()='删除']"))
        log.info("[page_ats] '是否要删除该应聘信息？—>确定")
        self.base_click((By.XPATH,"//span[text()='是否要删除该应聘信息？']/../div/a[text()='确 定']"))
        time.sleep(1)