from liufu_web_auto.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from liufu_web_auto.pages.bodong_login_page import BodongLogin
from liufu_web_auto.pages.bodong_home_page import Bongdong_home
import time

#漫画详情页
class Bodong_Details(Base):
    # 海量精品漫画第一部漫画详情页
    # 立即阅读按钮
    loc_read_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.detail-info-fix>div>div>div.detail-btn>a>span")
    #收藏按钮
    loc_save_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.detail-info-fix>div>div>div.detail-btn>a.blue>span")
    #已收藏按钮
    loc_complete_save =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.detail-info-fix>div>div>div.detail-btn>a.done>span")
    #第一集漫画
    loc_first = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-comic-list>div.comic-list>ul>li:nth-child(1)")
    #点击展开更多目录
    loc_get_more = (By.LINK_TEXT,"点击展开更多目录")
    #点击收起更多目录
    loc_stop_more = (By.LINK_TEXT,"点击收起更多目录")
    #点赞图标
    loc_like_iocn = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comment>div.mod-detail-comment>ul>li>div.commnet-detail-fix>div>div.info>a>i")
    #评论图标
    loc_comment_icon = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comment>div.mod-detail-comment>ul>li>div.commnet-detail-fix>div>div.info>a.comment>i")
    #以上为热门评论，前往波洞APP看更多内容
    loc_click_to_app = (By.LINK_TEXT,"以上为热门评论，前往波洞APP看更多内容")
    #去往app弹窗关闭按钮
    loc_close_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.dialog-guide>div>a")
    #弹窗app下载二维码
    loc_ercode =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.dialog-guide>div>div.main>p")
    #相关推荐漫画
    loc_first_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(1)")
    loc_second_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(2)")
    loc_third_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(3)")
    loc_fourth_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(4)")
    loc_fifth_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(5)")
    loc_sixth_commic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-recommend>div.mod-comic-list-vertical>ul>li:nth-child(6)")

    def get_title(self,title_name):
        title = self.is_title_contains(title_name)
        return title

    def complete_save_text(self):
        complete_save = self.get_text(self.loc_complete_save)
        return complete_save

    def save_button_text(self):
        save = self.get_text(self.loc_save_button)
        return save

    def get_more_text(self):
        get_more = self.get_text(self.loc_stop_more)
        return get_more

    def stop_more_text(self):
        stop_more = self.get_text(self.loc_get_more)
        return stop_more

    def ercode_text(self):
        ercode = self.get_text(self.loc_ercode)
        return ercode

    def read_button(self):
        '''点击立即阅读按钮'''
        self.click(self.loc_read_button)

    def save_button(self):
        '''点击收藏按钮'''
        self.click(self.loc_save_button)

    def cancel_save(self):
        self.click(self.loc_complete_save)

    def first(self):
        '''点击第一话漫画'''
        self.click(self.loc_first)

    def get_more(self):
        '''点击展开更多目录'''
        self.click(self.loc_get_more)

    def stop_more(self):
        '''点击收起更多目录'''
        self.click(self.loc_stop_more)

    def like_icon(self):
        '''点赞按钮'''
        self.click(self.loc_like_iocn)

    def comment_icon(self):
        '''评论按钮'''
        self.click(self.loc_comment_icon)

    def click_to_app(self):
        '''点击弹出，app二维码下载弹窗'''
        self.click(self.loc_click_to_app)

    def close_button(self):
        '''二维码下载弹窗关闭按钮'''
        self.click(self.loc_close_button)

    #相关推荐漫画
    def recommend_commic_first(self):
        self.click(self.loc_first_commic)

    def recommend_commic_second(self):
        self.click(self.loc_second_commic)

    def recommend_commic_third(self):
        self.click(self.loc_third_commic)

    def recommend_commic_fourth(self):
        self.click(self.loc_fourth_commic)

    def recommend_commic_fifth(self):
        self.click(self.loc_fifth_commic)

    def recommend_commic_sixth(self):
        self.click(self.loc_sixth_commic)

if __name__=='__main__':
    bodong_url = "https://boodo.qq.com/"
    driver = webdriver.Chrome()
    driver.get(bodong_url)
    driver.maximize_window()
    a = BodongLogin(driver)
    b = Bongdong_home(driver)
    c = Bodong_Details(driver)
    a.login()
    b.first_comic()
    time.sleep(10)
    c.swith_new_window()
    # all_windows = driver.window_handles
    # print(all_windows)
    # print(driver.current_window_handle)
    # r = c.get_title("第1话")
    # print(r)