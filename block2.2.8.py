from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By.NAME, "firstname").send_keys("Собака сутулая")
    browser.find_element(By.NAME, "lastname").send_keys("Собака сутулая")
    browser.find_element(By.NAME, "email").send_keys("yasosubibu@.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()