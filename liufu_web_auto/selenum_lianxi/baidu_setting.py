from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #鼠标悬停事件模块导入
from selenium.webdriver.support.select import Select #select模块导入定位下拉框
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()  #窗口最大化
driver.implicitly_wait(10)  #隐性等待时间设置
mouse = driver.find_element_by_xpath('.//div[@id = "u1"]/a[8]')
ActionChains(driver).move_to_element(mouse).perform()  #鼠标悬停
driver.find_element_by_link_text('搜索设置').click()
time.sleep(3)
#driver.find_element_by_xpath('.//select[@id = "nr"]/option[3]').click()  #第一种方法定位下拉框：直接xpath定位
s = driver.find_element_by_id("nr")
Select(s).select_by_index(1)  #通过下拉框索引值来定位
time.sleep(5)
Select(s).select_by_value("50") #通过下拉框选项值来定位
time.sleep(5)
Select(s).select_by_visible_text('每页显示10条') #通过下拉框文本值来定位
time.sleep(3)
s.click()
driver.find_element_by_xpath('.//div[@id = "gxszButton"]/a[1]').click()#点击保存设置
time.sleep(3)
a = driver.switch_to_alert()   #切换到alert弹窗
try:
    print(a.text)
    a.accept()
except:
    print("没有弹窗")

