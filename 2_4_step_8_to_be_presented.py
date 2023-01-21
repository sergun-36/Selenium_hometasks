from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


url = 'http://suninjuly.github.io/explicit_wait2.html'

def calculate_result(x):
	result = str(math.log(abs(12*math.sin(int(x)))))
	return result


try:
	browser = webdriver.Chrome()
	browser.get(url)
	

	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))
	book_button = browser.find_element(By.ID, 'book')
	book_button.click()

	x = browser.find_element(By.ID, 'input_value').text
	result = calculate_result(x)

	result_field = browser.find_element(By.ID, 'answer')
	result_field.send_keys(result)

	submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')#(By., 'button[type = "submit"]')
	submit.click()
	


finally:
	time.sleep(5)
	browser.quit()