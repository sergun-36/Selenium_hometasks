from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/cats.html'
try:
	browser = webdriver.Chrome()
	browser.get(url)
	browser.implicitly_wait(5)

	browser.find_element(By.ID, 'button')

finally:
	browser.quit()

