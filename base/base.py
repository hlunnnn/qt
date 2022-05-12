import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from base.getrootdirectory import GetRootDirectory


class Base:

    def __init__(self, driver):
        self.driver = driver


    def base_find_element(self, loc, timeout=2, poll=0.5):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_element(*loc))
        except TimeoutException as e:
            self.base_get_screenshot()
            print("查找元素超时了")

    def base_click(self, loc):
        # 点击
        self.base_find_element(loc).click()

    def base_send_keys(self, loc, value):

        self.base_find_element(loc).send_keys(value)

    def base_get_handle(self):
        #获取当前页的handle
        return self.driver.current_window_handle

    def base_switch_handle(self,handle):
        #获取当前页的handle
        self.driver.switch_to.window(handle)

    def base_get_text(self,loc):
        #返回元素的文本
        return  self.base_find_element(loc).text

    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file(GetRootDirectory.get_root_directory() +"/image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S", time.localtime())))

    def base_element_isexist(self,args):
        try:
            self.base_find_element(args)
            return True
        except:
            return False


    #切换到最新的窗口
    def base_switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def base_new_window(self):
        js = "window.open('');"
        self.driver.execute_script(js)
        self.base_switch_to_new_window()

    def base_close_window(self):
        # 关闭当前窗口
        self.driver.close()

    '''
        鼠标操作
    '''
    def base_mouse_moveto(self,loc):
        # 鼠标移动到某个元素
        ActionChains(self.driver).move_to_element(self.base_find_element(loc)).perform()

    '''
        键盘
    '''
    def base_keys_enter(self,loc):
        # 键盘敲回车
        self.base_send_keys(loc,Keys.ENTER)



    # def __init__(self,driver):
    #     log.info("[base]: 正在获取初始化driver对象：{}".format(driver))
    #     self.driver = driver
    #
    # def base_find(self,loc,timeout=5,poll=0.5):
    #
    #     log.info("[base]: 正在定位:{}元素".format(loc))
    #     try:
    #         return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
    #         # return self.driver.find_element(*loc)
    #     except Exception as e:
    #         log.error("错误:{}".format(e))
    #         raise e
    #
    #
    # def base_click(self,args):
    #     log.info("[base]: 开始对:{}元素实行点击事件".format(args))
    #     max_retry = 0
    #     while max_retry<=1:
    #         try:
    #             self.base_find(args).click()
    #             log.info("[base]: 对{}元素进行点击".format(args))
    #             break
    #         except Exception as e:
    #             log.info("[base]: 正在对{}元素点击异常，再次点击".format(args))
    #             print("异常了")
    #             log.error("错误:{}".format(e))
    #             raise e
    #         finally:
    #             max_retry+=1
    #
    #
    #
    # def base_sendkeys(self,args,value):
    #
    #     log.info("[base]: 正在对:{}元素输入:{}".format(args,value))
    #     self.base_find(args).send_keys(value)
    #
    # def base_gethtml(self,args):
    #     self.base_find(args).get_attribute('innerHTML')
    #
    # #判断元素是否存在  方法封装
    # def base_element_isexist(self,args):
    #     try:
    #         self.base_find(args)
    #         return True
    #     except:
    #         return False
    #
    # #键盘回车
    # def base_enter(self,args):
    #     log.info("[base]: 正在对:{}元素点击回车".format(args))
    #     self.base_find(args).send_keys(Keys.ENTER)
    #
    # #获取指定title页面的handle方法
    # def base_switch_to_window_by_title(self,title):
    #     #获取当前页面所有handles
    #     for handle in self.driver.window_handles:
    #         self.driver.switch_to.window(handle)
    #         if self.driver.title == title:
    #             return handle
    #
    # # 获取指定title页面的handle方法
    # def base_switch_to_window_by_handle(self, handle):
    #     log.info("[base]: 获取页面的handle:{}".format(handle))
    #     self.driver.switch_to.window(handle)
    #
    # #切换到最新的窗口
    # def base_switch_to_new_window(self):
    #     log.info("[base]: 切换到最新打开的窗口}")
    #     windows = self.driver.window_handles
    #     self.driver.switch_to.window(windows[-1])
    #
    # # 获取当前窗口句柄
    # def base_get_handle(self):
    #     log.info("[base]: 获取当前窗口句柄}")
    #     return self.driver.current_window_handle
    #
    # #获取文本方法,返回元素文本信息
    # def base_get_text(self,loc):
    #     log.info("[base]: 正在获取:{}元素文本值".format(loc))
    #     return self.base_find(loc).text
    #
    #
    #
    # #截图方法
    # def base_get_image(self):
    #     self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d  %H_%M_%S")))
    #
    # #新开窗口访问
    # def base_new_window(self):
    #     js = "window.open('');"
    #     self.driver.execute_script(js)
    #     self.base_switch_to_new_window()
    # #清空
    # def base_clear(self,loc):
    #     el = self.base_find(loc)
    #     el.send_keys(Keys.CONTROL, 'a')
    #     el.send_keys(Keys.BACKSPACE)
    #
    # #关闭窗口
    # def base_close_window(self):
    #     self.driver.close()