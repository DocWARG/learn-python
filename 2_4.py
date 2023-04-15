from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
 
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(15)
price = browser.find_element(By.CSS_SELECTOR, '#price')
while price.text != '$100':
    price = browser.find_element(By.CSS_SELECTOR, '#price')

browser.find_element(By.CSS_SELECTOR, "#book").click()
x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").get_attribute('innerHTML'))
y = math.log(abs(12*math.sin(x)))
browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "#solve").click()
time.sleep(30)
browser.quit()