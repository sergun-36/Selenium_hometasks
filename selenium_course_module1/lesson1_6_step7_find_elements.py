from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

try:
	url = "http://suninjuly.github.io/huge_form.html"

	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(url)

	elements = browser.find_elements(By.CSS_SELECTOR, "input")
	for element in elements:
		element.send_keys("Мой ответ")

	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()
finally:
	time.sleep(30)
	browser.quit()