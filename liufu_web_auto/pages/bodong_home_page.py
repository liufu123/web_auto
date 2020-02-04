from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.bodong_login_page import BodongLogin
import time
class Bongdong_home(Base):
    #搜索框
    loc_search_input = (By.ID,"search-input")
    #搜索按钮
    loc_search_button =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-topbar>div>form.topbar-search>input:nth-child(2)")
    #收藏按钮
    loc_save = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div>div>ul>li.collect>div")
    #我要投稿
    loc_submit = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div>div>ul>li:nth-child(2)>a")
    #下载app
    loc_download_app = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div>div>ul>li.download>a")
    # #海量精品漫画
    # loc_more_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div>span")
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
    loc_read_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-comic>div>div.book-hd-cnt>div>div.detail-btn>a>span")
    #海量精品漫画第一部漫画
    loc_first_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-comic>div.mod-comic>ul>li>div")
    # #热门人气新番
    # loc_hot_new_comic = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div>span")
    #热门人气新番第一步动画
    loc_first_anime = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-anime>div.mod-anime>ul>li>section>a")
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
    # loc_create =(By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div>span")
    loc_cosplay = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(1)")
    loc_dongman = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(2)")
    loc_zhoubian = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(3)")
    loc_huihua = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(4)")
    loc_youxi = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(5)")
    loc_yanshengxiaoshuo = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(6)")
    loc_shenghuo = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(7)")
    loc_shengyin = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(8)")
    loc_modaozushi = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(9)")
    loc_huyaoxiaohongniang = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(10)")
    loc_wangzherongyao = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(11)")
    loc_chiji = (By.CSS_SELECTOR, "#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div>span:nth-child(12)")
    loc_create_all_fenlei = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.mod-typebar>div.typebar-item>a")
    #查看更多
    loc_more_button = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.panel-ugc>div.biz-ugc>div>div>a")
    #绝对领域
    loc_jueduilingyu = (By.CSS_SELECTOR,"#app>div>div.pc-main-wrap>div.pc-main-cnt>div.dialog-ugc>div>div.dialog-bd>div>h3")

    def text(self):
        r = self.get_text(self.loc_jueduilingyu)
        return r

    def save(self):
        '''点击收藏'''
        self.click(self.loc_save)

    def submit(self):
        '''点击我要投稿'''
        self.click(self.loc_submit)

    def download_app(self):
        '''点击下载APP'''
        self.click(self.loc_download_app)

    def search(self,search_input="狐妖小红娘"):
        '''搜索框搜索'''
        self.sendKeys(self.loc_search_input,search_input)
        self.click(self.loc_search_button)

    # def more_comic_all(self):
    #     self.js_focus(self.loc_more_comic)
    #海量精品漫画
    def lianai(self):
        '''点击恋爱'''
        self.click(self.loc_lianai)

    def hougong(self):
        '''点击后宫'''
        self.click(self.loc_hougong)

    def zhenmei(self):
        '''点击臻美'''
        self.click(self.loc_zhenmei)

    def chuanyue(self):
        '''点击穿越'''
        self.click(self.loc_chuanyue)

    def shaonv(self):
        '''点击少女'''
        self.click(self.loc_shaonv)

    def xuanhuan(self):
        '''点击玄幻'''
        self.click(self.loc_xuanhuan)

    def gufeng(self):
        '''点击古风'''
        self.click(self.loc_gufeng)

    def kongbu(self):
        '''点击恐怖'''
        self.click(self.loc_kongbu)

    def gaoxiao(self):
        '''点击搞笑'''
        self.click(self.loc_gaoxiao)

    def rexue(self):
        '''点击热血'''
        self.click(self.loc_rexue)

    def wanjie(self):
        '''点击完结'''
        self.click(self.loc_wanjie)

    def riman(self):
        '''点击日漫'''
        self.click(self.loc_riman)

    def guoman(self):
        '''点击国漫'''
        self.click(self.loc_guoman)

    def hanman(self):
        '''点击韩漫'''
        self.click(self.loc_hanman)

    def meiman(self):
        '''点击美漫'''
        self.click(self.loc_meiman)

    def xiaoyuan(self):
        '''点击校园'''
        self.click(self.loc_xiaoyuan)

    def all_fenlei(self):
        '''点击全部分类'''
        self.click(self.loc_all_fenlei)

    def read_button(self):
        '''点击开始阅读按钮'''
        self.click(self.loc_read_button)

    def first_comic(self):
        '''点击海量精品漫画第一部漫画'''
        self.click(self.loc_first_comic)

    # def hot_comic_all(self):
    #     self.js_focus(self.loc_hot_new_comic)
    #热门人气新番
    def first_anime(self):
        '''点击第一部动画'''
        self.click(self.loc_first_anime)

    def maoxian(self):
        '''点击冒险'''
        self.click(self.loc_maoxian)

    def zhandou(self):
        '''点击战斗'''
        self.click(self.loc_zhandou)

    def hot_gaoxiao(self):
        '''点击搞笑'''
        self.click(self.loc_hot_gaoxiao)

    def jingdian(self):
        '''点击经典'''
        self.click(self.loc_jingdian)

    def kehuan(self):
        '''点击科幻'''
        self.click(self.loc_kehuan)

    def hot_xuanhuan(self):
        '''点击玄幻'''
        self.click(self.loc_hot_xuanhuan)

    def mohuan(self):
        '''点击魔幻'''
        self.click(self.loc_mohuan)

    def wuxia(self):
        '''点击武侠'''
        self.click(self.loc_wuxia)

    def jingji(self):
        '''点击竞技'''
        self.click(self.loc_jingji)

    def hot_lianai(self):
        '''点击恋爱'''
        self.click(self.loc_hot_lianai)

    def tuili(self):
        '''点击推理'''
        self.click(self.loc_tuili)

    def zhiyu(self):
        '''点击治愈'''
        self.click(self.loc_zhiyu)

    def tengxunchupin(self):
        '''点击腾讯出品'''
        self.click(self.loc_tengxunchupin)

    def qita(self):
        '''点击其他'''
        self.click(self.loc_qita)

    def hot_all_fenlei(self):
        '''点击全部分类'''
        self.click(self.loc_hot_all_fenlei)

    # def create_content(self):
    #     self.js_focus(self.loc_create)
    # 创作大触云集
    def cosplay(self):
        '''点击cosplay'''
        self.click(self.loc_cosplay)

    def dongman(self):
        '''点击动漫'''
        self.click(self.loc_dongman)

    def zhoubian(self):
        '''点击周边'''
        self.click(self.loc_zhoubian)

    def huihua(self):
        '''点击绘画'''
        self.click(self.loc_huihua)

    def youxi(self):
        '''点击游戏'''
        self.click(self.loc_youxi)

    def yanshengxiaoshuo(self):
        '''点击衍生小说'''
        self.click(self.loc_yanshengxiaoshuo)

    def shenghuo(self):
        '''点击生活'''
        self.click(self.loc_shenghuo)

    def shengyin(self):
        '''点击声音'''
        self.click(self.loc_shengyin)

    def modaozushi(self):
        '''点击魔道祖师'''
        self.click(self.loc_modaozushi)

    def huyaoxiaohongniang(self):
        '''点击狐妖小红娘'''
        self.click(self.loc_huyaoxiaohongniang)

    def wangzherongyao(self):
        '''点击王者荣耀'''
        self.click(self.loc_wangzherongyao)

    def chiji(self):
        '''点击吃鸡'''
        self.click(self.loc_chiji)

    # def yingxionglianmeng(self):
    #     self.click(self.loc_yingxionglianmeng)

    def create_all_fenlei(self):
        '''点击全部分类'''
        self.click(self.loc_create_all_fenlei)

    def more_button(self):
        '''点击查看更多'''
        self.click(self.loc_more_button)


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


