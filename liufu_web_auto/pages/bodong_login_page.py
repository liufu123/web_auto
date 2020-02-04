from liufu_web_auto.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from liufu_web_auto.common.read_ini import Read_ini
bodong_url = "https://boodo.qq.com/"
config = Read_ini()
class BodongLogin(Base):
    loc_login = (By.CSS_SELECTOR,'div.cnt>ul.topbar-nav>li:nth-child(5)>div')
    loc_QQlogin = (By.CSS_SELECTOR,'#app>div>div.pc-main-wrap>div.pc-topbar>div>ul>li.login>div>div>div>a:nth-child(1)')
    loc_iframe = (By.ID,'login_frame')
    loc_user_psw = (By.CSS_SELECTOR, '#switcher_plogin')
    loc_login_username = (By.CSS_SELECTOR, '#u')
    loc_login_password = (By.CSS_SELECTOR, '#p')
    loc_login_button = (By.CSS_SELECTOR, '#login_button')
    loc_qqtouxiang = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div>div>ul>li.login-avatar>div>img")
    loc_get_username = (By.CSS_SELECTOR,'#app>div>div.pc-main-wrap>div>div>ul>li.login-avatar>div>div>p')


    def login_ready(self):
        self.mouse(self.loc_login)
        time.sleep(5)
        self.click(self.loc_QQlogin)
        self.swith_iframe(self.loc_iframe)
        time.sleep(1)
        self.click(self.loc_user_psw)

    def input_username(self,username='2500000095'):
        self.sendKeys(self.loc_login_username,username)

    def input_psw(self,psw='456789'):
        self.sendKeys(self.loc_login_password,psw)

    def click_login_button(self):
        self.click(self.loc_login_button)

    def login(self):
        self.login_ready()
        self.input_username()
        self.input_psw()
        self.click_login_button()

    def get_name(self):
        self.mouse(self.loc_qqtouxiang)
        time.sleep(3)
        user = self.get_text(self.loc_get_username)
        return user

    def is_login_sucess(self,text):
        return self.is_text(self.loc_get_username,text)

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get(bodong_url)
    time.sleep(3)
    driver.maximize_window()
    bodong = BodongLogin(driver)
    bodong.login()

