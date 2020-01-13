from selenium import webdriver
import time

driver = webdriver.Chrome()
#driver.delete_all_cookies()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(20)
c1 = {u'domain': u'.baidu.com',
      u'expiry': 1819811365.73916,
      u'httpOnly': True,
      u'name': u'BDUSS',
      u'path': u'/',
      u'secure': False,
      u'value': u'kttU0RwOWZFUkUxMmVSM3Nic3NQRnAtdDNackZQMmZlSi13Zk9zTGthZ2tseXhkSUFBQUFBJCQAAAAAAAAAAAEAAADyTuyRvfC6xb3Hyc-83AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACQKBV0kCgVdd'}

c2 = {u'domain': u'www.baidu.com',
      u'expiry': 1561475367,
      u'httpOnly': False,
      u'name': u'BD_UPN',
      u'path': u'/',
      u'secure': False,
      u'value': u'12314353'}

c3 = {u'domain': u'www.baidu.com',
      u'httpOnly': False,
      u'name': u'BD_HOME',
      u'path': u'/',
      u'secure': False,
      u'value': u'1'}
driver.add_cookie(c1)
driver.add_cookie(c2)
driver.add_cookie(c3)
time.sleep(5)
driver.refresh()
driver.find_element_by_xpath('//*[@id="u_sp"]/a[1]').click()
window1 = driver.current_window_handle
driver.find_element_by_link_text('共同开创中朝两党两国关系的美好未来').click()
all_window = driver.window_handles
for i in all_window:
      if i == window1:
            driver.find_element_by_link_text('北京网络媒体红色故土福建行').click()
            print(driver.title)
      else:
            driver.close()

time.sleep(10)
driver.quit()

