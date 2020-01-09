from selenium import webdriver

browser = webdriver.Chrome()
browser.get(url='http://www.baidu.com/')
browser.save_screenshot('baidu.png')
print(browser.page_source)