import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element=browser.find_element(By.ID, "treasure")
    x=x_element.get_attribute('valuex')
    y=str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
   
    time.sleep(5)
    browser.quit()
