import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects2.html')

    a=browser.find_element(By.ID, "num1")
    num1=a.text
    b=browser.find_element(By.ID, "num2")
    num2=b.text
    x=str(int(num1)+int(num2))
    S = Select(browser.find_element(By.ID, "dropdown"))
    S.select_by_value(x)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
   
    time.sleep(30)
    browser.quit()
