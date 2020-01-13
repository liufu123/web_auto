from selenium import webdriver
import unittest
from liufu_web_auto.pages.zendao_login_page import Zendao_Login
from liufu_web_auto.pages.zendao_addbug_page import Add_bug

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drever = webdriver.Chrome()
        cls.drever.maximize_window()
        cls.a = Zendao_Login(cls.drever)
        cls.b = Add_bug(cls.drever)

    def setUp(self):
        #self.a.is_alert_exit()
        self.drever.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.drever.refresh()

    def test01(self):
        self.a.login()
        name = self.a.get_name()
        self.assertTrue(name == "退出")

    def test02(self):
        self.a.input_username()
        self.a.input_psw("111111")
        self.a.login_button()
        self.a.is_alert_exit()
        # name = self.a.get_name()
        # self.assertTrue(name == "")

    def test03(self):
        self.a.forget_psw()
        title = self.a.is_title("忘记密码 - 禅道")
        self.assertTrue(title)

    def test04(self):
        self.a.login()
        self.b.addbug("liufu测试","000000000000000000")

    def tearDown(self):
        self.drever.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.drever.quit()


if __name__ == "__main__":
    unittest.main()
