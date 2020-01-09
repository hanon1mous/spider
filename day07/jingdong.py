from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.jd.com/')
browser.find_element_by_id('key').send_keys('python')
browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
time.sleep(2)
s_list = browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
for pro in s_list:
    print(pro.text.split('\n')[:4])

