import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_lesson6_step10(unittest.TestCase):
    def test_lesson6_step10_1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,"//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,"//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,"//input[@class='form-control third' and @required]")
        input3.send_keys("yasosubibu.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text)
        browser.quit()     
    def test_lesson6_step10_2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,"//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,"//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,"//input[@class='form-control third' and @required]")
        input3.send_keys("yasosubibu.com")
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text)
        browser.quit()       

if __name__ == "__main__":
    unittest.main()