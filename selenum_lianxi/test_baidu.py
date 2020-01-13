from selenium import webdriver
import unittest
import time

class BaiduTest(unittest.TestCase):
    """百度首页自动化"""
    def test_baidu(self):
        """登录百度，点击导航条、搜索python"""
        #创建ChromeOptions对象，直接用本地的Google打开Chrome
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--user-data-dir = C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')
        self.driver = webdriver.Chrome(options=self.option)
        driver = self.driver
        driver.get('http://www.baidu.com')
        #窗口最大化
        driver.maximize_window()
        #设置隐性等待时间
        driver.implicitly_wait(20)
        #跳过登录验证所需要的cookie信息
        self.c1 = {u'domain': u'.baidu.com',
                   u'expiry': 1819811365.73916,
                   u'httpOnly': True,
                   u'name': u'BDUSS',
                   u'path': u'/',
                   u'secure': False,
                   u'value': u'kttU0RwOWZFUkUxMmVSM3Nic3NQRnAtdDNackZQMmZlSi13Zk9zTGthZ2tseXhkSUFBQUFBJCQAAAAAAAAAAAEAAADyTuyRvfC6xb3Hyc-83AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACQKBV0kCgVdd'}

        self.c2 = {u'domain': u'www.baidu.com',
                   u'expiry': 1561475367,
                   u'httpOnly': False,
                   u'name': u'BD_UPN',
                   u'path': u'/',
                   u'secure': False,
                   u'value': u'12314353'}

        self.c3 = {u'domain': u'www.baidu.com',
                   u'httpOnly': False,
                   u'name': u'BD_HOME',
                   u'path': u'/',
                   u'secure': False,
                   u'value': u'1'}
        #添加cookie
        driver.add_cookie(self.c1)
        driver.add_cookie(self.c2)
        driver.add_cookie(self.c3)
        time.sleep(5)
        #刷新
        driver.refresh()
        try:
            self.text = driver.find_element_by_xpath('//*[@id="s_username_top"]/span').text
            if self.text == u'金号角上架':
                print('登录成功')
                time.sleep(3)
        except:
            print('登录失败')
            driver.quit()
        #获取当前窗口话柄
        self.window = driver.current_window_handle
        #点击新闻
        driver.find_element_by_xpath('//*[@id="u_sp"]/a[1]').click()
        time.sleep(3)
        driver.switch_to.window(self.window)  #切换回第一个窗口
        #点击hao123
        driver.find_element_by_xpath('//*[@id="u_sp"]/a[2]').click()
        time.sleep(3)
        driver.switch_to.window(self.window)
        # #点击地图
        driver.find_element_by_xpath('//*[@id="u_sp"]/a[3]').click()
        driver.switch_to.window(self.window)
        #点击视频
        driver.find_element_by_xpath('//*[@id="u_sp"]/a[4]').click()
        driver.switch_to.window(self.window)
        #搜索python
        driver.find_element_by_id('kw').send_keys('python')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        title = driver.title
        try:
            self.assertEqual(title,u'python_百度搜索')
            driver.quit()
        except:
            print('搜索内容不符合预期')

if __name__ == '__main__':
    #unittest.main()识别类中的以test_xxx命名的函数
    unittest.main()