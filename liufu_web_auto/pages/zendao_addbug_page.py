from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.zendao_login_page import Zendao_Login
import os
pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#项目工程路径E:\liufu-selenium\
file_name = os.path.join(pro_path,"common","文件上传.exe")
zendao_url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class Add_bug(Base):
    loc_test_button =(By.CSS_SELECTOR,"#mainmenu>ul>li:nth-child(4)")#测试
    loc_bug_button =(By.CSS_SELECTOR,"#modulemenu>ul>li:nth-child(2)")#bug
    loc_addbug_button =(By.CSS_SELECTOR,"#featurebar>div>div:nth-child(2)>div>a")#提交bug
    loc_trunk =(By.XPATH,'//*[@id="openedBuild_chosen"]/ul')#影响版本
    loc_trunk_add =(By.XPATH,'//*[@id="openedBuild_chosen"]/div/ul/li')#默认版本trunk
    loc_bug_title =(By.XPATH,'//*[@id="title"]')#bug标题
    loc_bug_pic =(By.XPATH,'//*[@id="dataform"]/table/tbody/tr[6]/td/div[2]/div[1]/span[18]')#图片
    loc_add_pic_button =(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div/div[3]/form/div/div')#浏览本地图片
    loc_sure_pic =(By.XPATH,'/html/body/div[3]/div[1]/div[3]/span[1]')#确定按钮
    loc_input_body =(By.CSS_SELECTOR,".article-content")#bug内容
    loc_save_button =(By.CSS_SELECTOR,"#submit")#保存按钮
    loc_iframe =(By.CSS_SELECTOR,".ke-edit-iframe")

    def test_button(self):
        '''点击测试按钮'''
        self.click(self.loc_test_button)

    def bug_button(self):
        '''点击bug按钮'''
        self.click(self.loc_bug_button)

    def addbug_button(self):
        '''点击提交bug按钮'''
        self.click(self.loc_addbug_button)

    def trunk(self):
        '''点击影响版本'''
        self.click(self.loc_trunk)

    def trunk_add(self):
        '''选择影响版本trunk'''
        self.click(self.loc_trunk_add)

    def input_title(self,text):
        '''输入bug标题'''
        self.sendKeys(self.loc_bug_title,text)

    def bug_pic(self):
        '''点击图片按钮'''
        self.click(self.loc_bug_pic)

    def add_bug_pic(self):
        '''点击里浏览，添加本地图片'''
        self.click(self.loc_add_pic_button)

    def sure_pic(self):
        '''点击图片确定按钮'''
        self.click(self.loc_sure_pic)

    def input_body(self,text):
        '''输入bug内容'''
        self.clear(self.loc_input_body)
        self.sendKeys(self.loc_input_body,text)

    def save(self):
        '''点击bug保存按钮'''
        self.click(self.loc_save_button)

    def exe(self):
        '''执行exe'''
        os.system(file_name)

    def addbug(self,title="自动化测试bug标题",body="自动化测试bug内容输入"):
        '''bug添加流程'''
        self.test_button()
        self.bug_button()
        self.addbug_button()
        self.trunk()
        self.trunk_add()
        self.input_title(title)
        self.bug_pic()
        self.add_bug_pic()
        self.exe()
        self.sure_pic()
        self.swith_iframe(self.loc_iframe)
        self.input_body(body)
        self.driver.switch_to_default_content()
        self.js_roll_down()
        self.save()


if __name__ =="__main__":
    driver = webdriver.Chrome()
    driver.get(zendao_url)
    driver.maximize_window()
    a = Add_bug(driver)
    b = Zendao_Login(driver)
    b.login()
    a.addbug()




