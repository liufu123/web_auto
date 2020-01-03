from selenium import webdriver
from common.readExcel import Excel_read
import time
import unittest
import ddt
import os

pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))#项目工程路径E:\liufu-selenium\
file_name = os.path.join(pro_path,"common","testdata.xlsx")
print(file_name)
data = Excel_read(file_name)
testdatas = data.dict_data()
print(testdatas)

@ddt.ddt
class Baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    @ddt.data(*testdatas)
    def test01(self,data):
        self.driver.find_element_by_id('kw').send_keys(data["内容"])
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        title = self.driver.title
        self.assertEqual(data["结果"],title)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()




