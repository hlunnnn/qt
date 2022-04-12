import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import page
from base.base import Base
from base.get_logger import GetLogger


log = GetLogger().get_logger()

class PagePositionList(Base):

    #搜索职位关键字
    def plist_ss_pos_name(self,name):
        log.info("[page_PagePositionalList] 组件一搜索职位名称，点击全部")
        self.base_sendkeys((By.CLASS_NAME,"search-ipt"),name)
        self.base_enter((By.CLASS_NAME,"search-ipt"))
        time.sleep(1)
        return self.plist_position_list_compare("pos-name", name)

    #搜索职位工作地点
    def plist_ss_pos_locate(self):
        log.info("[page_PagePositionalList] 组件一搜索工作地点，点击全部")
        self.base_click(page.position_place_search)
        log.info("[page_PagePositionalList] 搜索的选项为{}".format(self.base_get_text(page.position_place_item)))
        self.base_click(page.position_place_item)
        time.sleep(1)
        return self.plist_position_list_compare("pos-locate","北京市")

    #搜索职位职位类别
    def plist_ss_pos_cate(self):
        log.info("[page_PagePositionalList] 组件一搜索职位类别，点击全部")
        self.base_click(page.position_type_search)
        # time.sleep(2)
        log.info("[page_PagePositionalList] 全部点击完毕")
        log.info("[page_PagePositionalList] 搜索的选项为{}".format(self.base_get_text(page.position_type_item)))
        self.base_click(page.position_type_item)
        time.sleep(1)
        return self.plist_position_list_compare("pos-cate","NGS研发类")
    #搜索职位所属机构
    def plist_ss_pos_company(self):
        log.info("[page_PagePositionalList] 组件一搜所属机构，点击全部")
        self.base_click(page.position_organ_search)
        log.info("[page_PagePositionalList] 搜索的选项为{}".format(self.base_get_text(page.position_organ_item)))
        self.base_click(page.position_organ_item)
        time.sleep(1)
        return self.plist_position_list_compare("pos-company","公司机构测试")
    #搜索薪酬
    def plist_ss_pos_salary(self):
        log.info("[page_PagePositionalList] 组件一搜索薪酬范围，点击全部")
        self.base_click(page.position_salary_search)
        log.info("[page_PagePositionalList] 搜索的选项为{}".format(self.base_get_text(page.position_salary_item)))
        self.base_click(page.position_salary_item)
        time.sleep(1)
        return self.plist_position_list_compare("pos-salary","1000-2000/月")

    #比较职位列表第一页字段的值
    def plist_position_list_compare(self,field,value):

        if field=="pos-name":
            val = self.base_get_text((By.XPATH, "//div[@class='list-box']/div[2]/div[@class='list-cell pos-name']/span"))
            if value in val:return True
            else:return False

        if field=="pos-locate":
            val = self.base_get_text((By.XPATH, "//div[@class='list-box']/div[2]/div[@class='list-cell pos-locate']/span"))
            if value in val:return True
            else:return False
        if field=="pos-cate":  #职位类别
            val = self.base_get_text((By.XPATH, "//div[@class='list-box']/div[2]/div[@class='list-cell pos-cate']/span"))
            print(val)
            if value == val:return True
            else:return False
        if field=="pos-company":
            val = self.base_get_text((By.XPATH, "//div[@class='list-box']/div[2]/div[@class='list-cell pos-company']/span"))
            if value == val:return True
            else:return False
        if field=="pos-salary":
            val = self.base_get_text((By.XPATH, "//div[@class='list-box']/div[2]/div[@class='list-cell pos-salary']/span"))
            if value == val:return True
            else:return False






    #进入社会招聘
    def plist_to_social(self):
        self.base_click((By.XPATH, "//ul[@class='navbar']/li[2]"))
    #进入校园
    def plist_to_campus(self):
        self.base_click((By.XPATH, "//ul[@class='navbar']/li[3]"))

    #投递职位
    #type：social、campus   招聘类型
    def plist_deliver_position(self,name):

        log.info("[page_PagePositionalList] 搜索职位关键字：{}".format(name))
        self.base_clear((By.CLASS_NAME,"search-ipt"))
        self.plist_ss_pos_name(name)

        current_handle = self.base_get_handle()
        time.sleep(1)
        log.info("[page_PagePositionalList] 点击搜索的第一个职位：{}".format(name))
        self.base_click((By.XPATH,"//div[@class='list-box']/div[2]"))
        time.sleep(2)
        log.info("[page_PagePositionalList] 切换到职位详情窗口")
        self.base_switch_to_new_window()
        log.info("[page_PagePositionalList] 点击立即投递")
        self.base_click((By.XPATH,"//div[@class='pos-detail-hd-wrap']//button[@class='deliver']"))
        log.info("[page_PagePositionalList] 勾选协议")
        time.sleep(1)
        self.base_click((By.XPATH,"//label[@class='ant-checkbox-wrapper']/span"))
        log.info("[page_PagePositionalList] 点击确认提交")
        self.base_click((By.XPATH,"//span[text()='确认提交']/.."))
        time.sleep(2)
        log.info("[page_PagePositionalList] 关闭职位详情窗口")
        self.driver.close()
        log.info("[page_PagePositionalList] 切换回职位列表的handle")
        self.base_switch_to_window_by_handle(current_handle)

    #投递站点职位
    def plist_deliver_position_station(self,name):

        self.plist_ss_pos_name(name)
        self.base_click((By.XPATH,"//div[@class='list-box']/div[2]"))
        time.sleep(2)
        self.base_switch_to_new_window()
        self.base_click((By.XPATH,"//div[@class='pos-detail-hd-wrap']//button[@class='deliver']"))
        self.base_click((By.XPATH,"//span[text()='确认并下一步']/.."))
        #选择第一个站点
        self.base_click((By.XPATH,"//div[@class='siteRadio']//label[1]/span"))
        self.base_click((By.XPATH,"//label[@class='ant-checkbox-wrapper']/span/input"))   #勾选协议
        self.base_click((By.XPATH,"//span[text()='确认提交']/.."))
        time.sleep(2)
        self.base_close_window()





if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(page.index_url)
    driver.maximize_window()




