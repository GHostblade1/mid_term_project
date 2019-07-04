from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.set_window_size(width=1920, height=1080)
url = 'www.baidu.com'

