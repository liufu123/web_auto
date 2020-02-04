from selenium import webdriver
import unittest
import time
from liufu_web_auto.common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
c1 = {u'domain': u'.baidu.com',
      u'expiry': 1819811365.73916,
      u'httpOnly': True,
      u'name': u'BDUSS',
      u'path': u'/',
      u'secure': False,
      u'value': u'kttU0RwOWZFUkUxMmVSM3Nic3NQRnAtdDNackZQMmZlSi13Zk9zTGthZ2tseXhkSUFBQUFBJCQAAAAAAAAAAAEAAADyTuyRvfC6xb3Hyc-83AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACQKBV0kCgVdd'}

c2 = {u'domain': u'www.baidu.com',
                   u'expiry': 1561475367,
                   u'httpOnly': False,
                   u'name': u'BD_UPN',
                   u'path': u'/',
                   u'secure': False,
                   u'value': u'12314353'}

c3 = {u'domain': u'www.baidu.com',
                   u'httpOnly': False,
                   u'name': u'BD_HOME',
                   u'path': u'/',
                   u'secure': False,
                   u'value': u'1'}
class Baidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         cls.driver = webdriver.Chrome()
         cls.driver.get('http://www.baidu.com')
         cls.a = Base(cls.driver)
         cls.driver.maximize_window()
         cls.windows = cls.driver.current_window_handle
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''登录百度'''
        self.driver.add_cookie(c1)
        self.driver.add_cookie(c2)
        self.driver.add_cookie(c3)
        time.sleep(3)
        self.driver.refresh()
        try:
            self.text = self.driver.find_element_by_xpath('//*[@id="s_username_top"]/span').text
            if self.text == u'金号角上架':
                print('登录成功')
        except:
            print('登录失败')

    def test_02(self):
        '''点击导航栏'''
        self.news = (By.XPATH,'//*[@id="u_sp"]/a[1]')#点击新闻
        self.hao123 = (By.XPATH,'//*[@id="u_sp"]/a[2]')#点击hao123
        self.map = (By.XPATH,'//*[@id="u_sp"]/a[3]')#点击地图
        self.video =(By.XPATH,'//*[@id="u_sp"]/a[4]')#点击视频
        self.a.click(self.news)
        self.driver.switch_to.window(self.windows)
        self.a.click(self.hao123)
        self.driver.switch_to.window(self.windows)
        self.a.click(self.map)
        self.driver.switch_to.window(self.windows)
        self.a.click(self.video)
        self.driver.switch_to.window(self.windows)

    def test_03(self):
        '''输入内容点击搜索'''
        self.loc1 = (By.ID,'kw')
        self.loc2 = (By.ID,'su')
        self.a.sendKeys(self.loc1,'python')
        self.a.click(self.loc2)
        time.sleep(3)
        self.title = self.driver.title
        try:
            self.assertEqual(self.title, u'python_百度搜索')
            print('搜索成功')
        except:
            print(self.title)
            print('搜索内容不符合预期')

if __name__ == '__main__':
    unittest.main()




