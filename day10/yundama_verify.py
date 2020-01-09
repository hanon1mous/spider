from selenium import webdriver
from PIL import Image
import pytesseract
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.yundama.com/')
browser.save_screenshot('index.png')
location = browser.find_element_by_xpath('//*[@id="verifyImg"]').location
size = browser.find_element_by_xpath('//*[@id="verifyImg"]').size
img = Image.open('index.png')
x1 = location['x']
y1 = location['y']
x2 = x1 + size['width']
y2 = y1 + size['height']
capt = img.crop((x1, y1, x2, y2))
result = pytesseract.image_to_string(capt)
print(result)
capt.save('capt.png')

print(location, size)