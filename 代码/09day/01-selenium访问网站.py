from selenium import webdriver
import time

url = 'https://www.baidu.com/'
driver = webdriver.Chrome(
    executable_path='/Users/xiaoyuan/Downloads/chromedriver'
)
driver.get(url)
with open('baidu.html', 'w') as f:
    f.write(driver.page_source)
input = driver.find_element_by_id('kw')
time.sleep(1)
input.send_keys('美女')
time.sleep(1)
btn = driver.find_element_by_id('su')
btn.click()
time.sleep(3)
driver.save_screenshot('baidu.png')
btn = driver.find_element_by_class_name('n')
btn.click()
