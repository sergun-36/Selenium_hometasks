from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

url = "http://suninjuly.github.io/find_xpath_form"

try:
	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(url)
	elements = browser.find_elements(By.CSS_SELECTOR, "input")
	for element in elements:
		element.send_keys("Мой ответ")

	button = browser.find_element(By.XPATH, "//button[@type='submit']")
	button.click()
finally:
	time.sleep(30)
	browser.quit()