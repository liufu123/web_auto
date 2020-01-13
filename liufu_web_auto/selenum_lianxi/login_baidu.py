from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.get('http://www.baidu.com')
driver.maximize_window()
cookie1 = driver.get_cookies()
print('登录前cookie:',cookie1)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[7]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('Example')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('Password')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
time.sleep(60)

cookie2 = driver.get_cookies()
print('登录后cookie:',cookie2)
time.sleep(3)
driver.quit()

