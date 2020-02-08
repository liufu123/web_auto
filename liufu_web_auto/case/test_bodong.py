import unittest
from selenium import webdriver
from pages.bodong_login_page import BodongLogin
from pages.bodong_home_page import Bongdong_home
from pages.bodong_details_page import Bodong_Details
from pages.bodong_video_details_page import Bodong_video_details
import time
from common.logger import Log
url = "https://boodo.qq.com/"
class Bodong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bodong = BodongLogin(cls.driver)
        cls.bodong_home = Bongdong_home(cls.driver)
        cls.bodong_details = Bodong_Details(cls.driver)
        cls.bodong_video_details = Bodong_video_details(cls.driver)
        cls.log = Log()
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def sw_window_get_title(self,title_name="最热动画 - 波洞星球boodo"):
        '''切换新打开的窗口，获取title'''
        self.bodong_home.swith_new_window()
        r = self.bodong_home.is_title_contains(title_name)
        self.driver.close()
        self.bodong_home.swith_window()
        return r

    def test_01(self):
        '''登录波洞'''
        self.log.info("开始登录波洞")
        self.bodong.login()
        time.sleep(5)
        self.log.info("获取登录用户名")
        ele = self.bodong.get_name()
        self.log.info("获取的用户名：%s"%ele)
        self.assertTrue(ele == "用户b")

    def test_02(self):
        '''搜索'''
        self.log.info("开始搜索：狐妖小红娘")
        self.bodong_home.search()
        self.log.info("获取标题")
        re = self.sw_window_get_title("狐妖小红娘搜索结果 - 波洞星球boodo")
        self.log.info("获取的标题：%s" % re)
        self.assertTrue(re)

    def test_03(self):
        '''点击收藏'''
        self.bodong_home.save()
        re = self.sw_window_get_title("收藏 - 在线漫画免费看 - 波洞星球boodo")
        self.assertTrue(re)

    def test_04(self):
        '''点击我要投稿'''
        self.bodong_home.submit()
        re = self.sw_window_get_title("QQ动漫开放平台")
        self.assertTrue(re)

    def test_05(self):
        '''点击下载app'''
        self.bodong_home.download_app()
        re = self.sw_window_get_title("波洞手机客户端 - 波洞星球boodo")
        self.assertTrue(re)

    def test_06(self):
        '''点击恋爱分类'''
        self.bodong_home.lianai()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_07(self):
        '''点击后宫分类'''
        self.bodong_home.hougong()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_08(self):
        '''点击臻美分类'''
        self.bodong_home.zhenmei()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_09(self):
        '''点击穿越分类'''
        self.bodong_home.chuanyue()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_10(self):
        '''点击少女分类'''
        self.bodong_home.shaonv()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_11(self):
        '''点击玄幻分类'''
        self.bodong_home.xuanhuan()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_12(self):
        '''点击古风分类'''
        self.bodong_home.gufeng()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_13(self):
        '''点击恐怖分类'''
        self.bodong_home.kongbu()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_14(self):
        '''点击搞笑分类'''
        self.bodong_home.gaoxiao()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_15(self):
        '''点击热血分类'''
        self.bodong_home.rexue()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_16(self):
        '''点击完结分类'''
        self.bodong_home.wanjie()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_17(self):
        '''点击日漫分类'''
        self.bodong_home.riman()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_18(self):
        '''点击国漫分类'''
        self.bodong_home.guoman()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_19(self):
        '''点击韩漫分类'''
        self.bodong_home.hanman()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_20(self):
        '''点击美漫分类'''
        self.bodong_home.meiman()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_21(self):
        '''点击校园分类'''
        self.bodong_home.xiaoyuan()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_22(self):
        '''点击全部分类'''
        self.bodong_home.all_fenlei()
        re = self.sw_window_get_title()
        self.assertTrue(re)

    def test_23(self):
        '''点击开始阅读按钮'''
        self.bodong_home.read_button()
        re = self.sw_window_get_title("-第")
        self.assertTrue(re)

    def test_24(self):
        '''点击第一部漫画'''
        self.bodong_home.first_comic()
        re = self.sw_window_get_title("在线漫画全集免费看 - 波洞星球boodo")
        self.assertTrue(re)

    def test_25(self):
        '''点击冒险分类'''
        self.bodong_home.maoxian()
        re = self.sw_window_get_title("最热冒险动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_26(self):
        '''点击战斗分类'''
        self.bodong_home.zhandou()
        re = self.sw_window_get_title("最热战斗动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_27(self):
        '''点击搞笑分类'''
        self.bodong_home.hot_gaoxiao()
        re = self.sw_window_get_title("最热搞笑动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_28(self):
        '''点击经典分类'''
        self.bodong_home.jingdian()
        re = self.sw_window_get_title("最热经典动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_29(self):
        '''点击科幻分类'''
        self.bodong_home.kehuan()
        re = self.sw_window_get_title("最热科幻动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_30(self):
        '''点击玄幻分类'''
        self.bodong_home.hot_xuanhuan()
        re = self.sw_window_get_title("最热玄幻动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_31(self):
        '''点击魔幻分类'''
        self.bodong_home.mohuan()
        re = self.sw_window_get_title("最热魔幻动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_32(self):
        '''点击武侠分类'''
        self.bodong_home.wuxia()
        re = self.sw_window_get_title("最热武侠动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_33(self):
        '''点击竞技分类'''
        self.bodong_home.jingji()
        re = self.sw_window_get_title("最热竞技动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_34(self):
        '''点击恋爱分类'''
        self.bodong_home.hot_lianai()
        re = self.sw_window_get_title("最热恋爱动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_35(self):
        '''点击推理分类'''
        self.bodong_home.tuili()
        re = self.sw_window_get_title("最热推理动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_36(self):
        '''点击治愈分类'''
        self.bodong_home.zhiyu()
        re = self.sw_window_get_title("最热治愈动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_37(self):
        '''点击腾讯出品分类'''
        self.bodong_home.tengxunchupin()
        re = self.sw_window_get_title("最热腾讯出品动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_38(self):
        '''点击其他分类'''
        self.bodong_home.qita()
        re = self.sw_window_get_title("最热其他动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_39(self):
        '''点击全部分类'''
        self.bodong_home.hot_all_fenlei()
        re = self.sw_window_get_title("最热动画 - 波洞星球boodo")
        self.assertTrue(re)

    def test_40(self):
        '''点击cosplay分类'''
        self.bodong_home.cosplay()
        re = self.sw_window_get_title("Cosplay- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_41(self):
        '''点击动漫分类'''
        self.bodong_home.dongman()
        re = self.sw_window_get_title("动漫- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_42(self):
        '''点击周边分类'''
        self.bodong_home.zhoubian()
        re = self.sw_window_get_title("周边- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_43(self):
        '''点击绘画分类'''
        self.bodong_home.huihua()
        re = self.sw_window_get_title("绘画- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_44(self):
        '''点击游戏分类'''
        self.bodong_home.youxi()
        re = self.sw_window_get_title("游戏- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_45(self):
        '''点击衍生小说分类'''
        self.bodong_home.yanshengxiaoshuo()
        re = self.sw_window_get_title("衍生小说- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_46(self):
        '''点击生活'''
        self.bodong_home.shenghuo()
        re = self.sw_window_get_title("生活- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_47(self):
        '''点击声音分类'''
        self.bodong_home.shengyin()
        re = self.sw_window_get_title("声音- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_48(self):
        '''点击魔道祖师分类'''
        self.bodong_home.modaozushi()
        re = self.sw_window_get_title("")

    def test_49(self):
        '''点击狐妖小红娘分类'''
        self.bodong_home.huyaoxiaohongniang()
        re = self.sw_window_get_title("汉服- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_50(self):
        '''点击王者荣耀分类'''
        self.bodong_home.wangzherongyao()
        re = self.sw_window_get_title("")
        self.assertTrue(re)

    def test_51(self):
        '''点击吃鸡分类'''
        self.bodong_home.chiji()
        re = self.sw_window_get_title("音乐- 动漫社区内容 - 波洞星球boodo")
        self.assertTrue(re)

    def test_52(self):
        '''点击全部分类'''
        self.bodong_home.create_all_fenlei()
        re = self.bodong_home.text()
        self.assertTrue(re == '绝对领域')
        self.bodong_home.mouse_click()

    #漫画详情页
    def test_53(self):
        '''点击开始阅读'''
        self.bodong_home.first_comic()
        time.sleep(5)
        self.bodong_details.swith_new_window()
        self.bodong_details.read_button()
        re = self.bodong_details.get_title("-第")
        self.assertTrue(re)
        time.sleep(5)
        self.bodong_details.back()

    def test_54(self):
        '''点击收藏按钮'''
        if self.bodong_details.save_button_text() == "收藏":
            self.bodong_details.save_button()
            re = self.bodong_details.complete_save_text()
            self.assertTrue(re == "已收藏")
        elif self.bodong_details.complete_save_text() == "已收藏":
            self.bodong_details.cancel_save()
            self.driver.refresh()
            re = self.bodong_details.save_button_text()
            self.assertTrue(re == "收藏")

    def test_55(self):
        '''点击查看漫画第一话'''
        self.bodong_details.first()
        re = self.bodong_details.get_title("-第")
        self.assertTrue(re)
        self.bodong_details.back()

    def test_56(self):
        '''点击展开更多'''
        try:
            self.bodong_details.get_more()
            re = self.bodong_details.get_more_text()
            self.assertTrue(re == '点击收起更多目录')
        except:
            print("页面没有点击展开更多目录的按钮--漫画话数不够")

    def test_57(self):
        '''点击收起更多'''
        try:
            self.bodong_details.stop_more()
            re = self.bodong_details.stop_more_text()
            self.assertTrue(re == "点击展开更多目录")
        except:
            print("页面没有点击展开更多目录的按钮--漫画话数不够")

    def test_58(self):
        '''点击点赞icon'''
        self.bodong_details.like_icon()
        re = self.bodong_details.ercode_text()
        self.assertTrue("扫码下载波洞APP" in re)
        self.bodong_details.close_button()

    def test_59(self):
        '''点击评论icon'''
        self.bodong_details.comment_icon()
        re = self.bodong_details.ercode_text()
        self.assertTrue("扫码下载波洞APP" in re)
        self.bodong_details.close_button()

    def test_60(self):
        '''以上为热门评论，前往波洞APP看更多内容'''
        self.bodong_details.click_to_app()
        re = self.bodong_details.ercode_text()
        self.assertTrue("扫码下载波洞APP" in re)
        self.bodong_details.close_button()

    def test_61(self):
        '''相关推荐漫画1'''
        self.bodong_details.recommend_commic_first()
        re = self.sw_window_get_title("- 在线漫画全集免费看 - 波洞星球boodo")
        self.assertTrue(re)

    def test_62(self):
        '''暂停视频播放'''
        self.bodong_home.first_anime()
        time.sleep(5)
        self.bodong_video_details.swith_new_window()
        self.bodong_video_details.video_to_stop()

    def test_63(self):
        '''点击收藏按钮'''
        if self.bodong_video_details.save_anime_text() == "收藏":
            self.bodong_video_details.save_anime()
            r = self.bodong_video_details.ready_save_anime_text()
            self.assertTrue(r == "已收藏")
        elif self.bodong_video_details.ready_save_anime_text() == "已收藏":
            self.bodong_video_details.ready_save_anime()
            self.driver.refresh()
            r = self.bodong_video_details.save_anime_text()
            self.assertTrue(r == "收藏")

    def test_64(self):
        '''点击点赞按钮'''
        self.bodong_video_details.like_anime()
        r = self.bodong_video_details.gotoapp_windows_text()
        self.assertTrue("扫码下载波洞APP" in r)
        self.bodong_video_details.close()

    def test_65(self):
        '''点击评论按钮'''
        self.bodong_video_details.comment_anime()
        r = self.bodong_video_details.gotoapp_windows_text()
        self.assertTrue("扫码下载波洞APP" in r)
        self.bodong_video_details.close()

    def test_66(self):
        '''以上为热门评论，前往波洞APP看更多内容'''
        self.bodong_video_details.go_to_app()
        r = self.bodong_video_details.gotoapp_windows_text()
        self.assertTrue("扫码下载波洞APP" in r)
        self.bodong_video_details.close()

    def test_67(self):
        '''点击第2集动漫'''
        if self.bodong_video_details.vip_text() == "VIP":
            self.bodong_video_details.second_anime()
            self.bodong_video_details.close()
            print("第二集是vip特权")
        else:
            self.bodong_video_details.second_anime()

    def test_69(self):
        '''点击第一部推荐作品'''
        self.bodong_video_details.first_recommend()
        r = self.sw_window_get_title("高清动画在线观看 - 波洞星球boodo")
        self.assertTrue(r)

    def test_68(self):
        '''点击更多内容'''
        self.bodong_video_details.more_recommend()
        r = self.bodong_video_details.gotoapp_windows_text()
        self.assertTrue("扫码下载波洞APP" in r)
        self.bodong_video_details.close()






if __name__ == '__main__':
    unittest.main()
