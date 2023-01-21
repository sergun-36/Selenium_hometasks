import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/redirect_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(url)

	troll_button = browser.find_element(By.CLASS_NAME, 'trollface')
	troll_button.click()

	new_tab = browser.window_handles[1] #find new windows name
	browser.switch_to.window(new_tab) # switch to new tab

	x = browser.find_element(By.ID, 'input_value').text
	result = str(math.log(abs(12*math.sin(int(x)))))

	result_field = browser.find_element(By.ID, 'answer')
	result_field.send_keys(result)

	submit = browser.find_element(By.TAG_NAME, 'button')#(By., 'button[type = "submit"]')
	submit.click()



finally:
	time.sleep(5)
	browser.quit()