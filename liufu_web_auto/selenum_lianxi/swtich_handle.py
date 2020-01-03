from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_link_text('新闻').click()
print(driver.title)
time.sleep(5)
h1 = driver.current_window_handle  #获取当前窗口句柄
driver.find_element_by_xpath('.//*[@id = "pane-news"]/div/ul/li[1]').click()
print(driver.title)
all = driver.window_handles #获取所有窗口句柄
driver.switch_to.window(all[-1])
time.sleep(3)
a = driver.find_elements_by_xpath('.//*[@class = "nav-box"]/div[@class = "nav-li"]/a')
a[0].click()
print(driver.title)

def close_window():   #关闭当前打开的窗口
    all = driver.window_handles
    print(all)
    for i in all:
        if i != h1:
            driver.switch_to.window(all[-1])
            driver.close()
            all = driver.window_handles

close_window()
driver.switch_to.window(h1)
driver.back()

