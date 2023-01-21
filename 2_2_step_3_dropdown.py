from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()

browser.get(url)

num1 = int(browser.find_element(By.ID, 'num1').text)
num2 = int(browser.find_element(By.ID, 'num2').text)
result = num1+ num2

browser.find_element(By.TAG_NAME, 'select').click()
browser.find_element(By.CSS_SELECTOR, f'[value="{result}"]').click()

browser.find_element(By.TAG_NAME, 'button').click()


print(result)
time.sleep(10)
browser.quit()