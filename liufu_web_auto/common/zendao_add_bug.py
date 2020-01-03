from common.base import Base
from selenium.webdriver.common.by import By
from selenium import webdriver
class Zendao_add_bug(Base):
    #登录定位
    loc1 = (By.CSS_SELECTOR,'#account')
    loc2 = (By.CSS_SELECTOR, 'input[name=password]')
    loc3 = (By.XPATH, "//*[@id='submit']")
    #添加bug定位
    loc_test = (By.LINK_TEXT,'测试')
    loc_bug = (By.CSS_SELECTOR, '#subNavbar>ul>li>a')
    loc_tijiaobug = (By.CSS_SELECTOR,'#mainMenu>div.pull-right>a:nth-child(4)')
    loc_banben = (By.CSS_SELECTOR,'div#buildBox>div')
    loc_tjbanben = (By.CSS_SELECTOR, 'div#buildBox>div>div>ul')
    loc_title = (By.ID, 'title')  #输入bug标题
    loc_body = (By.CLASS_NAME, 'article-content') #输入bug正文
    loc_save = (By.CSS_SELECTOR, '#submit')


    def login(self,user="admin",psw="LFjj0918"):
        self.open_url('http://127.0.0.1/zentao/user-login.html')
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,psw)
        self.click(self.loc3)

    def add_bug(self):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_tijiaobug)
        self.click(self.loc_banben)
        self.click(self.loc_tjbanben)
        self.sendKeys(self.loc_title,"刘付的bug")
        self.iframe = self.driver.find_element_by_css_selector('iframe[class=ke-edit-iframe]')
        self.driver.switch_to.frame(self.iframe)
        # self.clear(self.loc_body)
        self.sendKeys(self.loc_body,'11111111111111111111111')
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    bug = Zendao_add_bug(driver)
    bug.login()
    bug.add_bug()



