import unittest
from selenium import webdriver
from liufu_web_auto.pages.bodong_login_page import BodongLogin
from liufu_web_auto.pages.bodong_home_page import Bongdong_home
import time
bodong_url = "https://boodo.qq.com/"
class Bodong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.bodong = BodongLogin(cls.driver)
        cls.bodong_home = Bongdong_home(cls.driver)
        cls.driver.get(bodong_url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

    def test_01(self):
        '''登录波洞'''
        self.bodong.login()
        time.sleep(5)
        ele = self.bodong.get_name()
        self.assertTrue(ele == "用户b")

    def test_02(self):
        '''搜索'''
        self.bodong_home.search()
        self.bodong_home.search()
        self.bodong_home.swith_not_first_window()
        r = self.bodong_home.is_title("狐妖小红娘搜索结果 - 波洞星球boodo")
        self.assertTrue(r == True)
        self.bodong_home.swith_window()

    def test_03(self):
        '''点击恋爱分类'''
        self.bodong_home.lianai()

    def test_04(self):
        self.bodong_home.hougong()

    def test_05(self):
        self.bodong_home.zhenmei()

    def test_06(self):
        self.bodong_home.chuanyue()

    def test_07(self):
        self.bodong_home.shaonv()

    def test_08(self):
        self.bodong_home.xuanhuan()

    def test_09(self):
        self.bodong_home.gufeng()

    def test_10(self):
        self.bodong_home.kongbu()

    def test_11(self):
        self.bodong_home.gaoxiao()

    def test_12(self):
        self.bodong_home.rexue()

    def test_13(self):
        self.bodong_home.wanjie()

    def test_14(self):
        self.bodong_home.riman()

    def test_15(self):
        self.bodong_home.guoman()

    def test_16(self):
        self.bodong_home.hanman()

    def test_17(self):
        self.bodong_home.meiman()

    def test_18(self):
        self.bodong_home.xiaoyuan()

    def test_19(self):
        self.bodong_home.more_comic_all()

    def test_20(self):
        self.bodong_home.read_button()

    def test_21(self):
        self.bodong_home.first_comic()

    def test_22(self):
        self.bodong_home.maoxian()

    def test_23(self):
        self.bodong_home.zhandou()

    def test_24(self):
        self.bodong_home.hot_gaoxiao()

    def test_25(self):
        self.bodong_home.jingdian()

    def test_26(self):
        self.bodong_home.kehuan()

    def test_27(self):
        self.bodong_home.hot_xuanhuan()

    def test_28(self):
        self.bodong_home.mohuan()

    def test_29(self):
        self.bodong_home.wuxia()

    def test_30(self):
        self.bodong_home.jingji()

    def test_31(self):
        self.bodong_home.hot_lianai()

    def test_32(self):
        self.bodong_home.tuili()

    def test_33(self):
        self.bodong_home.zhiyu()

    def test_34(self):
        self.bodong_home.tengxunchupin()

    def test_35(self):
        self.bodong_home.qita()

    def test_36(self):
        self.bodong_home.hot_all_fenlei()

    def test_37(self):
        self.bodong_home.cosplay()

    def test_38(self):
        self.bodong_home.dongman()

    def test_39(self):
        self.bodong_home.zhoubian()

    def test_40(self):
        self.bodong_home.huihua()

    def test_41(self):
        self.bodong_home.youxi()

    def test_42(self):
        self.bodong_home.yanshengxiaoshuo()

    def test_43(self):
        self.bodong_home.shenghuo()

    def test_44(self):
        self.bodong_home.shengyin()

    def test_45(self):
        self.bodong_home.modaozushi()

    def test_46(self):
        self.bodong_home.huyaoxiaohongniang()

    def test_47(self):
        self.bodong_home.wangzherongyao()

    def test_48(self):
        self.bodong_home.chiji()

    def test_49(self):
        self.bodong_home.yingxionglianmeng()

    # def test_50(self):
    #     self.bodong_home.create_all_fenlei()

    def test_51(self):
        self.bodong_home.more_button()

if __name__ == '__main__':
    unittest.main()
