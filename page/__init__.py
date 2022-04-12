from selenium.webdriver.common.by import By

index_url = "https://otwecruit.hotjob.cn/SU614405027e379f0001c451ba/pb/index.html#/"

#切换账号输入
login_change = By.CSS_SELECTOR,"span[class='wtspeicon wtspeicon-login wtspeicon-login-computer computerIcon']"
#code
login_code = By.ID,"corpCode"
#用户名
login_username = By.ID,"userName"
#密码
login_password = By.ID,"password"
#确认登录
login_button = By.ID,"loginImg"


#500职位搜索条件
position_name_search=By.XPATH,"//input[contains(@placeholder,'请搜索职位')]" #职位名称

position_place_search = By.XPATH,"//div[@class='categories']//div[@title='工作地点']/../ul//div"   #工作地点
position_place_item = By.XPATH,"//ul[@id='workPlace$Menu']/li[text()='北京市']"
position_type_search= By.XPATH,"//div[@class='categories']//div[@title='职位类别']/../ul//div"  #职位类别
position_type_item = By.XPATH,"//ul[@id='postType$Menu']/li[text()='NGS研发类']"
position_organ_search=By.XPATH,"//div[@class='categories']//div[@title='公司/部门']/../ul//div" #公司
position_organ_item = By.XPATH,"//ul[@id='orgName$Menu']/li[text()='公司机构测试']"
position_station_search=By.XPATH,"//div[@class='categories']//div[@title='站点']/../ul//div" #站点
position_station_item=By.XPATH,"//ul[@id='site$Menu']/li[text()='苏州大学']" #站点
position_salary_search=By.XPATH,"//div[@class='categories']//div[@title='薪酬范围']/../ul//div" #薪酬
position_salary_item=By.XPATH,"//ul[@id='salary$Menu']/li[text()='1000-2000/月']" #薪酬
position_education_search=By.XPATH,"//div[@class='categories']//div[@title='学历要求']/../ul//div" #学历要求
position_education_item=By.XPATH,"//ul[@id='education$Menu']/li[text()='硕士研究生']" #学历要求
position_time_search=By.XPATH,"//div[@class='categories']//div[@title='发布时间']/../ul//div" #发布时间
position_time_item=By.XPATH,"//ul[@id='releaseTime$Menu']/li[text()='今天']" #发布时间
position_item_search=By.XPATH,"//div[@class='categories']//div[@title='招聘项目']/../ul//div" #招聘项目
position_item_item=By.XPATH,"//ul[@id='recruitmentPro$Menu']/li[text()='6月招聘项目']" #招聘项目


