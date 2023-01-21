import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(url)

browser.execute_script('document.title="Script executing";alert("RObot at work");')

time.sleep(6)
browser.quit()