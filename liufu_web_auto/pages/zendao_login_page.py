from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
zendao_url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class Zendao_Login(Base):
    loc_login_username = (By.ID,"account")
    loc_login_psw = (By.XPATH,'//*[@id="login-form"]/form/table/tbody/tr[2]/td/input')
    loc_keep_login = (By.CSS_SELECTOR,"#keepLoginon")
    loc_login_button = (By.CSS_SELECTOR,"#submit")
    loc_forget_psw = (By.LINK_TEXT,"忘记密码")
    loc_name = (By.CSS_SELECTOR,"#topnav>a:nth-child(2)")


    def input_username(self,username="admin"):
        self.sendKeys(self.loc_login_username,username)

    def input_psw(self,psw='123456'):
        self.sendKeys(self.loc_login_psw,psw)

    def keep_login(self):
        self.click(self.loc_keep_login)

    def login_button(self):
        self.click(self.loc_login_button)

    def forget_psw(self):
        self.click(self.loc_forget_psw)

    def get_name(self):
        user = self.get_text(self.loc_name)
        return user

    def login(self):
        '''输入正确的帐号、密码->点击保持登录->点击登录'''
        self.input_username()
        self.input_psw()
        self.keep_login()
        self.login_button()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(zendao_url)
    driver.maximize_window()
    time.sleep(1)
    a = Zendao_Login(driver)
    a.login()
    b = a.get_name()
    print(b)
