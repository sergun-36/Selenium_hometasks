import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/alert_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(url)

	button = browser.find_element(By.TAG_NAME, 'button')
	button.click()

	alert = browser.switch_to.alert
	alert.accept()

	x = browser.find_element(By.ID, 'input_value').text
	result = str(math.log(abs(12*math.sin(int(x)))))

	result_field = browser.find_element(By.ID, 'answer')
	result_field.send_keys(result)

	submit = browser.find_element(By.TAG_NAME, 'button')#(By., 'button[type = "submit"]')
	submit.click()



finally:
	time.sleep(10)
	browser.quit()