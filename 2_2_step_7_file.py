import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

url = 'http://suninjuly.github.io/file_input.html'
first_name = 'test_first_name'
last_name = 'test_last_name'
email = 'test@email.com'

try:
	browser = webdriver.Chrome()
	browser.get(url)

	input_first_name = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
	input_first_name.send_keys(first_name)

	input_last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
	input_last_name.send_keys(last_name)

	input_email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
	input_email.send_keys(email)

	attach_field = browser.find_element(By.CSS_SELECTOR, 'input[name="file"]')
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'test_file.txt')           # добавляем к этому пути имя файла 
	attach_field.send_keys(file_path)

	submit = browser.find_element(By.TAG_NAME, 'button')
	submit.click()


finally:

	time.sleep(10)
	browser.quit()

"""
creation file in Python script
with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file
"""