from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

url = "http://suninjuly.github.io/registration1.html"
first_name = "First_name"
last_name = "Last_name"
email = "email@gmail.com"
expected_text = "Congratulations! You have successfully registered!"

try:
	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(url)
	first_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
	first_name_field.send_keys(first_name)
	last_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
	last_name_field.send_keys(last_name)
	email_field = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
	email_field.send_keys(email)

	submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	submit_button.click()

	#wait loading page
	time.sleep(1)
	#looking for  element with text
	welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
	#write to variable
	welcome_text = welcome_text_elt.text

	#compare
	assert expected_text == welcome_text

finally:
	time.sleep(10)
	browser.quit()