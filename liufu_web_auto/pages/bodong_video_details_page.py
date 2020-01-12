from liufu_web_auto.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from liufu_web_auto.pages.bodong_login_page import BodongLogin
from liufu_web_auto.pages.bodong_home_page import Bongdong_home
import time

#动漫详情页
class Bodong_video_details(Base):
    #视频播放地址
    loc_video = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.ui-clfx>div>div>section>div>div#player_2_0>txpdiv>txpdiv.txp_video_fit_cover>video")
    #收藏动漫按钮
    loc_save_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.ui-clfx>div>div>div>div>div.detail-btn>a>span")
    #已收藏动漫按钮
    lco_ready_save_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.ui-clfx>div>div>div>div>div.detail-btn>a.done>span")
    #点赞按钮
    loc_like_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.panel-comment>div.mod-detail-comment>ul>li>div.commnet-detail-fix>div>div.info>a.like")
    #评论按钮
    loc_comment_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.panel-comment>div.mod-detail-comment>ul>li>div.commnet-detail-fix>div>div.info>a.comment")
    #以上为热门评论，前往波洞APP看更多内容
    lco_go_to_app = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div>div>div.panel-comment>div.mod-detail-comment>div>a")
    #去往app弹窗关闭按钮
    loc_close = (By.CSS_SELECTOR,"body.firstscreen-loaded>div.dialog-guide>div>a.close")
    #去往app弹窗文案
    loc_gotoapp_windows_text = (By.CSS_SELECTOR,"body.firstscreen-loaded>div.dialog-guide>div>div.main>p")
    #第2集动漫
    loc_second_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.pc-anime-right>div>div.mod-catalog-list>ul.catalog-list>li:nth-child(2)>a")
    #vip图标
    loc_vip = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.pc-anime-right>div>div.mod-catalog-list>ul.catalog-list>li:nth-child(2)>span")
    #相关推荐栏第一部作品
    loc_first_recommend = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.pc-anime-right>div.panel-recommend>div.mod-recommend-list>ul>li>div>a")
    #更多推荐内容
    loc_more_recommend = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.pc-anime-right>div.panel-recommend>div.mod-recommend-list>div>a")

    def video_to_stop(self):
        '''播放10s后暂停播放'''
        time.sleep(10)
        self.video_stop_js(self.loc_video)

    def video_to_play(self):
        '''3s后播放视频'''
        time.sleep(10)
        self.video_play_js(self.loc_video)

    def save_anime(self):
        '''点击收藏按钮'''
        self.click(self.loc_save_anime)

    def save_anime_text(self):
        '''获取“收藏”文案并返回'''
        re = self.get_text(self.loc_save_anime)
        return re

    def ready_save_anime(self):
        '''点击已收藏按钮'''
        self.click(self.lco_ready_save_anime)

    def ready_save_anime_text(self):
        '''获取“已收藏”文案并返回'''
        re = self.get_text(self.lco_ready_save_anime)
        return re

    def like_anime(self):
        '''点击点赞按钮'''
        self.click(self.loc_like_anime)

    def comment_anime(self):
        '''点击评论按钮'''
        self.click(self.loc_comment_anime)

    def go_to_app(self):
        '''点击以上为热门评论，前往波洞APP看更多内容'''
        self.click(self.lco_go_to_app)

    def close(self):
        '''点击去往app弹窗关闭按钮'''
        self.click(self.loc_close)

    def gotoapp_windows_text(self):
        '''获取去往app弹窗文案'''
        re = self.get_text(self.loc_gotoapp_windows_text)
        return re

    def second_anime(self):
        '''点击动漫第二集'''
        self.click(self.loc_second_anime)

    def second_anime_text(self):
        '''获取动漫第二集文案：2'''
        re = self.get_text(self.loc_second_anime)
        return re

    def vip_text(self):
        '''获取vip文案'''
        re = self.get_text(self.loc_vip)
        return re

    def first_recommend(self):
        '''点击第一部推荐作品'''
        self.click(self.loc_first_recommend)

    def more_recommend(self):
        '''点击更多推荐内容'''
        self.click(self.loc_more_recommend)

if __name__=='__main__':
    bodong_url = "https://boodo.qq.com/"
    driver = webdriver.Chrome()
    driver.get(bodong_url)
    driver.maximize_window()
    a = BodongLogin(driver)
    b = Bongdong_home(driver)
    c = Bodong_video_details(driver)
    a.login()
    b.first_anime()
    c.swith_new_window()
    c.video_to_stop()
    c.video_to_play()
