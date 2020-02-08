from selenium import webdriver
import unittest
import time
from common.base import Base
from selenium.webdriver.common.by import By
from common.logger import Log
import ddt
from common.readExcel import Excel_read
import os
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

pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_name = os.path.join(pro_path, 'common',"testdata.xlsx")
data = Excel_read(file_name)
testdatas = data.dict_data()
print(testdatas)

@ddt.ddt
class Baidu(unittest.TestCase):
    loc1 = (By.ID, 'kw')
    loc2 = (By.ID, 'su')

    def baidu_search(self,content,result):
        self.a.sendKeys(self.loc1,content)
        self.a.click(self.loc2)
        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title,result)
        self.a.clear(self.loc1)

    @classmethod
    def setUpClass(cls):
         cls.driver = webdriver.Chrome()
         cls.driver.get('http://www.baidu.com')
         cls.a = Base(cls.driver)
         cls.log = Log()
         cls.driver.maximize_window()
         cls.windows = cls.driver.current_window_handle
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        '''登录百度'''
        self.log.info("添加cookie1")
        self.driver.add_cookie(c1)
        self.log.info("添加cookie2")
        self.driver.add_cookie(c2)
        self.log.info("添加cookie3")
        self.driver.add_cookie(c3)
        time.sleep(3)
        self.driver.refresh()
        self.log.info("开始登录操作")
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

    @ddt.data(*testdatas)
    def test_03(self,data):
        '''输入内容点击搜索'''
        self.baidu_search(data["content"],data["result"])

if __name__ == '__main__':
    unittest.main()




