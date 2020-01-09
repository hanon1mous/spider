from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.baidu.com/')
browser.find_element_by_id('kw').send_keys('杨幂')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.find_element_by_class_name('n').click()
time.sleep(3)

