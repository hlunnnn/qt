import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import page
from base.base import Base
from base.get_logger import GetLogger


log = GetLogger().get_logger()


class PagePersonal(Base):


    #进入个人中心
    def personal_to_personal(self):
        log.info("[page_Personal] 进入个人中心")
        self.base_click((By.CLASS_NAME,"user-box"))

    #点击修改志愿
    def personal_click_change_volunteer(self):
        log.info("[page_Personal] 点击修改志愿")
        self.base_click((By.CLASS_NAME,"change-btn"))
    #修改志愿
    def personal_change_volunteer(self,posname,n):
        log.info("[page_Personal] 准备修改志愿，应聘职位:{}".format(posname))
        self.base_click((By.XPATH, "//div[(@class='pos-name fl') and (contains(text(),'" + posname + "'))]/../div[2]/div"))
        # self.base_find((By.XPATH, "//div[(@class='pos-name fl') and (contains(text(),'" + posname + "'))]/../div[2]/div"))
        log.info("[page_Personal] 选择志愿")
        self.base_click((By.XPATH,"//ul[@role='listbox']/li[text()='"+n+"']"))
        log.info("[page_Personal] 点击确认更改，确认修改志愿")
        self.base_click((By.CLASS_NAME,"ant-btn ant-btn-primary"))

    #查看应聘记录志愿
    def personal_volunteer(self,name):
        self.base_get_text((By.XPATH,"//span[contains(text(),'"+name+"']/../span[contains(text(),'志愿']"))



    #创建简历
    def personal_add_resunme(self,name,email,mobile):
        log.info("[page_Personal] 点击创建简历")
        self.base_click((By.XPATH,"//p[@class='resumeEmptyBtn']"))
        log.info("[page_Personal] 窗口切换到简历操作页")
        self.base_switch_to_window_by_title("简历操作")
        self.base_sendkeys((By.XPATH,"//div[@id='11_2_0']/input"),name)  #姓名
        self.base_sendkeys((By.XPATH,"//div[@id='11_36_0']/input[@placeholder='输入手机号码']"),mobile)    #移动电话
        self.base_sendkeys((By.XPATH,"//div[@id='11_37_0']/input"),email)  #邮箱


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(page.index_url)
    driver.maximize_window()




