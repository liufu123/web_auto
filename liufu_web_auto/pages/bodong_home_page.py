from liufu_web_auto.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from liufu_web_auto.pages.bodong_login_page import BodongLogin
import time

class Bongdong_home(Base):
    #搜索框
    loc_search_input = (By.ID,"search-input")
    #搜索按钮
    loc_search_button =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-topbar>div>form.topbar-search>input:nth-child(2)")
    #海量精品漫画
    loc_more_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div>span")
    #漫画分类
    loc_lianai = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-typebar>div>span")
    loc_hougong = (By.LINK_TEXT,"后宫")
    loc_zhenmei = (By.LINK_TEXT,"耽美")
    loc_chuanyue = (By.LINK_TEXT,"穿越")
    loc_shaonv = (By.LINK_TEXT,"少女")
    loc_xuanhuan = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-typebar>div>span:nth-child(6)")
    loc_gufeng = (By.LINK_TEXT,"古风")
    loc_kongbu = (By.LINK_TEXT, "恐怖")
    loc_gaoxiao = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-typebar>div>span:nth-child(9)")
    loc_rexue = (By.LINK_TEXT, "热血")
    loc_wanjie = (By.LINK_TEXT, "完结")
    loc_riman = (By.LINK_TEXT, "日漫")
    loc_guoman = (By.LINK_TEXT, "国漫")
    loc_hanman = (By.LINK_TEXT, "韩漫")
    loc_meiman = (By.LINK_TEXT, "美漫")
    loc_xiaoyuan = (By.LINK_TEXT, "校园")
    loc_all_fenlei = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-typebar>div.typebar-item>a")
    #立即阅读
    loc_read_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-comic>div>div.book-hd-cnt>div>div.detail-btn>a")
    #海量精品漫画第一部漫画
    loc_first_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-comic>ul>li>div")
    #热门人气新番
    loc_hot_new_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div>span")
    #新番分类
    loc_maoxian = (By.LINK_TEXT, "冒险")
    loc_zhandou = (By.LINK_TEXT, "战斗")
    loc_hot_gaoxiao = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div.mod-typebar>div>span:nth-child(3)")
    loc_jingdian = (By.LINK_TEXT, "经典")
    loc_kehuan = (By.LINK_TEXT, "科幻")
    loc_hot_xuanhuan = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div.mod-typebar>div>span:nth-child(6)")
    loc_mohuan = (By.LINK_TEXT, "魔幻")
    loc_wuxia = (By.LINK_TEXT, "武侠")
    loc_jingji = (By.LINK_TEXT, "竞技")
    loc_hot_lianai = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div.mod-typebar>div>span:nth-child(10)")
    loc_tuili = (By.LINK_TEXT, "推理")
    loc_zhiyu = (By.LINK_TEXT, "治愈")
    loc_tengxunchupin = (By.LINK_TEXT, "腾讯出品")
    loc_qita = (By.LINK_TEXT, "其他")
    loc_hot_all_fenlei = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div.mod-typebar>div.typebar-item>a")
    #创作大触云集
    loc_create =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div>span")
    loc_cosplay = (By.LINK_TEXT, "COSPLAY")
    loc_dongman = (By.LINK_TEXT, "动漫")
    loc_zhoubian = (By.LINK_TEXT, "周边")
    loc_huihua = (By.LINK_TEXT, "绘画")
    loc_youxi = (By.LINK_TEXT, "游戏")
    loc_yanshengxiaoshuo = (By.LINK_TEXT, "衍生小说")
    loc_shenghuo = (By.LINK_TEXT, "生活")
    loc_shengyin = (By.LINK_TEXT, "声音")
    loc_modaozushi = (By.LINK_TEXT, "魔道祖师")
    loc_huyaoxiaohongniang = (By.LINK_TEXT, "狐妖小红娘")
    loc_wangzherongyao = (By.LINK_TEXT, "王者荣耀")
    loc_chiji = (By.LINK_TEXT, "吃鸡")
    loc_yingxionglianmeng = (By.LINK_TEXT, "英雄联盟")
    loc_create_all_fenlei = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div.typebar-item>a")
    #查看更多
    loc_more_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.biz-ugc>div>div>a>span")

    def get_title(self,title_name):
        title = self.is_title(title_name)
        return title

    def search(self,search_input="狐妖小红娘"):
        self.sendKeys(self.loc_search_input,search_input)
        self.click(self.loc_search_button)

    def more_comic_all(self):
        self.js_focus(self.loc_more_comic)

    def lianai(self):
        self.click(self.loc_lianai)
        #self.swith_window()

    def hougong(self):
        self.click(self.loc_hougong)
        self.swith_window()

    def zhenmei(self):
        self.click(self.loc_zhenmei)
        self.swith_window()

    def chuanyue(self):
        self.click(self.loc_chuanyue)
        self.swith_window()

    def shaonv(self):
        self.click(self.loc_shaonv)
        self.swith_window()

    def xuanhuan(self):
        self.click(self.loc_xuanhuan)
        self.swith_window()

    def gufeng(self):
        self.click(self.loc_gufeng)
        self.swith_window()

    def kongbu(self):
        self.click(self.loc_kongbu)
        self.swith_window()

    def gaoxiao(self):
        self.click(self.loc_gaoxiao)
        self.swith_window()

    def rexue(self):
        self.click(self.loc_rexue)
        self.swith_window()

    def wanjie(self):
        self.click(self.loc_wanjie)
        self.swith_window()

    def riman(self):
        self.click(self.loc_riman)
        self.swith_window()

    def guoman(self):
        self.click(self.loc_guoman)
        self.swith_window()

    def hanman(self):
        self.click(self.loc_hanman)
        self.swith_window()

    def meiman(self):
        self.click(self.loc_meiman)
        self.swith_window()

    def xiaoyuan(self):
        self.click(self.loc_xiaoyuan)
        self.swith_window()

    def all_fenlei(self):
        self.click(self.loc_all_fenlei)
        self.swith_window()

    def read_button(self):
        self.click(self.loc_read_button)
        self.swith_window()

    def first_comic(self):
        self.click(self.loc_first_comic)
        self.swith_window()

    def hot_comic_all(self):
        self.js_focus(self.loc_hot_new_comic)

    def maoxian(self):
        self.click(self.loc_maoxian)
        self.swith_window()

    def zhandou(self):
        self.click(self.loc_zhandou)
        self.swith_window()

    def hot_gaoxiao(self):
        self.click(self.loc_hot_gaoxiao)
        self.swith_window()

    def jingdian(self):
        self.click(self.loc_jingdian)
        self.swith_window()

    def kehuan(self):
        self.click(self.loc_kehuan)
        self.swith_window()

    def hot_xuanhuan(self):
        self.click(self.loc_hot_xuanhuan)
        self.swith_window()

    def mohuan(self):
        self.click(self.loc_mohuan)
        self.swith_window()

    def wuxia(self):
        self.click(self.loc_wuxia)
        self.swith_window()

    def jingji(self):
        self.click(self.loc_jingji)
        self.swith_window()

    def hot_lianai(self):
        self.click(self.loc_hot_lianai)
        self.swith_window()

    def tuili(self):
        self.click(self.loc_tuili)
        self.swith_window()

    def zhiyu(self):
        self.click(self.loc_zhiyu)
        self.swith_window()

    def tengxunchupin(self):
        self.click(self.loc_tengxunchupin)
        self.swith_window()

    def qita(self):
        self.click(self.loc_qita)
        self.swith_window()

    def hot_all_fenlei(self):
        self.click(self.loc_hot_all_fenlei)
        self.swith_window()

    def create_content(self):
        self.js_focus(self.loc_create)

    def cosplay(self):
        self.click(self.loc_cosplay)
        self.swith_window()

    def dongman(self):
        self.click(self.loc_dongman)
        self.swith_window()

    def zhoubian(self):
        self.click(self.loc_zhoubian)
        self.swith_window()

    def huihua(self):
        self.click(self.loc_huihua)
        self.swith_window()

    def youxi(self):
        self.click(self.loc_youxi)
        self.swith_window()

    def yanshengxiaoshuo(self):
        self.click(self.loc_yanshengxiaoshuo)
        self.swith_window()

    def shenghuo(self):
        self.click(self.loc_shenghuo)
        self.swith_window()

    def shengyin(self):
        self.click(self.loc_shengyin)
        self.swith_window()

    def modaozushi(self):
        self.click(self.loc_modaozushi)
        self.swith_window()

    def huyaoxiaohongniang(self):
        self.click(self.loc_huyaoxiaohongniang)
        self.swith_window()

    def wangzherongyao(self):
        self.click(self.loc_wangzherongyao)
        self.swith_window()

    def chiji(self):
        self.click(self.loc_chiji)
        self.swith_window()

    def yingxionglianmeng(self):
        self.click(self.loc_yingxionglianmeng)
        self.swith_window()

    def create_all_fenlei(self):
        self.click(self.loc_create_all_fenlei)
        self.swith_window()

    def more_button(self):
        self.js_roll_down()
        self.click(self.loc_more_button)
        self.swith_window()


if __name__=='__main__':
    bodong_url = "https://boodo.qq.com/"
    driver = webdriver.Chrome()
    driver.get(bodong_url)
    windows = driver.current_window_handle
    print(windows)
    driver.maximize_window()
    a = BodongLogin(driver)
    b = Bongdong_home(driver)
    a.login()
    b.lianai()
    b.lianai()
    all_windows = driver.window_handles
    print(all_windows)
    driver.switch_to.window(all_windows[1])
    print(driver.title)


