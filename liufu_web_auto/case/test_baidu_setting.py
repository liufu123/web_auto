from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #鼠标悬停事件模块导入
import unittest
from selenium.webdriver.common.by import By
from function.zendao_func import Zendao
from common.base import Base
import time
class Baidu_setting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()
        cls.alert = Zendao(cls.driver)
        cls.a = Base(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''百度设置'''
        time.sleep(1)
        mouse = self.driver.find_element_by_xpath('.//div[@id = "u1"]/a[8]')
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬停
        loc1 = (By.LINK_TEXT,'搜索设置')
        self.a.click(loc1)
        loc2 = (By.CSS_SELECTOR,"#nr>option:nth-child(3)")#定位选择每页50条
        self.a.click(loc2)
        loc3 = (By.CSS_SELECTOR,'#gxszButton>a:nth-child(1)')#点击保存设置
        self.a.click(loc3)
        self.alert.is_alert()


if __name__ == "__main__":
    unittest.main()


