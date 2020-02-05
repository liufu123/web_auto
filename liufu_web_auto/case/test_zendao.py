from selenium import webdriver
import unittest
from pages.zendao_login_page import Zendao_Login
from pages.zendao_addbug_page import Add_bug
from common.logger import Log
log = Log()
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
        log.info("禅道测试用例开始")
        self.a.login()
        log.info("开始登录禅道")
        name = self.a.get_name()
        log.info(u"获取的title内容：%s"%name)
        self.assertTrue(name == "退出")

    def test02(self):
        self.a.input_username()
        log.info("输入正确用户名")
        self.a.input_psw("111111")
        log.info("输入错误密码")
        self.a.login_button()
        log.info("点击登录按钮")
        self.a.is_alert_exit()
        log.info("关闭alert弹窗")
        # name = self.a.get_name()
        # self.assertTrue(name == "")

    def test03(self):
        self.a.forget_psw()
        log.info("点击忘记密码")
        title = self.a.is_title("忘记密码 - 禅道")
        log.info(u"获取的title内容：%s"%title)
        self.assertTrue(title)

    def test04(self):
        self.a.login()
        log.info("登录成功")
        self.b.addbug("liufu测试","000000000000000000")
        log.info("添加bug")

    def tearDown(self):
        self.drever.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.drever.quit()


if __name__ == "__main__":
    unittest.main()
