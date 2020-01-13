from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import yagmail
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.timeout = 30
        self.t = 0.5
        self.driver = driver

    def findelementNew(self,locator):
        '''定位元素，成功返回元素对象   不成功返回timeout'''
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
        return ele

    def findelement(self,locator):
        '''定位单个元素'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型！')
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findelements(self,locator):
        '''定位一组元素'''
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_elements(*locator))
        return ele

    def sendKeys(self,locator,text):
        '''文本输入'''
        ele = self.findelement(locator)
        ele.send_keys(text)

    def click(self,locator):
        '''按钮点击'''
        ele = self.findelement(locator)
        ele.click()

    def clear(self,locator):
        '''清空输入框'''
        ele = self.findelement(locator)
        ele.clear()

    def js_roll_down(self):
        '''滚动条滑动到最底部'''
        js_down = "var action=document.documentElement.scrollTop=10000"
        # js_down = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_down)

    def js_roll_top(self):
        '''滚动条滑动到最顶部'''
        js_top = "window.scrollTo(0,0)"
        self.driver.execute_script(js_top)

    def js_focus(self,locator):
        '''聚焦元素'''
        target = self.findelement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def video_play_js(self,locator):
        '''开始播放视频'''
        video = self.findelement(locator)
        self.driver.execute_script("arguments[0].play()",video)

    def video_stop_js(self,locator):
        '''暂停视频播放'''
        video = self.findelement(locator)
        self.driver.execute_script("arguments[0].pause()", video)

    def mouse(self,locator):
        '''鼠标悬停操作'''
        ele = self.findelement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def mouse_click(self,x=0,y=0):
        '''鼠标左键点击位置，x横坐标 y纵坐标'''
        ActionChains(self.driver).move_by_offset(x,y).click().perform()

    def swith_iframe(self,locator):
        '''切换iframe'''
        ele = self.findelement(locator)
        self.driver.switch_to.frame(ele)

    def open_url(self,url):
        '''打开网页'''
        self.driver.get(url)
        self.driver.maximize_window()

    def back(self):
        '''返回上一页'''
        self.driver.back()

    def forward(self):
        '''切换到下一页'''
        self.driver.forward()

    def swith_window(self):
        '''切换回首页窗口'''
        self.window = self.driver.window_handles
        self.driver.switch_to.window(self.window[0])

    def swith_new_window(self):
        '''切换到最新打开的窗口'''
        time.sleep(3)
        self.all_windows = self.driver.window_handles
        self.driver.switch_to.window(self.all_windows[-1])

    def is_title(self,title):
        '''判断期望title跟实际title是否一致  返回true false'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        '''判断实际title是否包含期望title  返回true false'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text(self,locator,text):
        '''判断文本是否一致 返回true false '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    def is_text_value(self, locator, value):
        '''判断元素中的value属性是否包含了预期的字符串 返回true false '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    def get_text(self,locator):
        '''获取文本'''
        try:
            ele = self.findelement(locator).text
            return ele
        except:
            return ""

    def is_alert(self):
        '''判断是否有alert弹窗  有alert返回alert对象  没有返回false'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def is_alert_exit(self):
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()

    def select_by_index(self,locator,index = 0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        ele = self.findelement(locator) #定位select
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        ele = self.findelement(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本值定位'''
        ele = self.findelement(locator)
        Select(ele).select_by_visible_text(text)



class Send_mail():
    '''发送邮件'''
    def send_mail(self,report):
        yag = yagmail.SMTP(user='Example@Example.com', password='Password', host='smtp.163.com')
        subject = "自动化测试报告"
        zhengwen = "请查看附件"
        yag.send('Example@Example.com', subject, contents=[zhengwen, report])
        print("邮件发送成功！")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://boodo.qq.com/')
    a = Base(driver)
    b = BodongLogin(driver)
    b.login()
    r = a.is_title("波洞星球boodo - 腾讯动漫画内容互动社区")
    print(r)