from selenium import webdriver
import unittest
from function.chandao_func import Login
import time
class Logincase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.zentao.net/user-login.html')
        cls.a = Login(cls.driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(self):
    #     self.driver.get('http://www.zentao.net/user-login.html')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_login_01(self):
        self.a.chandao_login('liufu123','lfjj0918')
        time.sleep(3)
        t = self.a.get_login_username()
        print('获取的结果：%s'%t)
        self.assertEqual(t, '刘付')

    def test_login_02(self):
        self.a.chandao_login('liufu123456','123456')
        time.sleep(3)
        t = self.a.get_login_username()
        print('错误的结果：%s'%t)
        self.assertEqual(t ,"")


if __name__ == '__main__':
    unittest.main()