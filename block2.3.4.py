from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element=browser.find_element(By.ID, "input_value")
    x = x_element.text
    y=calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()