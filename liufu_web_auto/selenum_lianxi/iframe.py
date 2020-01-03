from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://mail.126.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id('switchAccountLogin').click()
time.sleep(3)
iframe = driver.find_element_by_xpath('//div[@id = "loginDiv"]/iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_name('email').send_keys('11111111')
driver.switch_to.default_content()
try:
    driver.find_element_by_name('email').clear()
except:
    print('不在iframe内')

