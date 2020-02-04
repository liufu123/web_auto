'''
哔哩哔哩动画自动播放
'''
from selenium import webdriver
import time
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.bilibili.com/video/av16041375/")
video=WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#bilibiliPlayer>div>div>div.bilibili-player-video>video")))  # 找到视频
url=driver.execute_script("return arguments[0].currentSrc;",video)  # 打印视频地址
print(url)

print("start")
driver.execute_script("return arguments[0].play()",video)  # 开始播放
time.sleep(15)

print("stop")
driver.execute_script("return arguments[0].pause()",video) # 暂停



