from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/wait1.html'
success_message = 'successful'

try:
	browser = webdriver.Chrome()
	browser.get(url)
	browser.implicitly_wait(5) #waiting load of element , checking each 500ms not more 5 sc

	#time.sleep(1)

	button = browser.find_element(By.ID, 'verify')
	button.click()

	message = browser.find_element(By.ID, 'verify_message')

	assert success_message in message.text

finally:
	browser.quit()