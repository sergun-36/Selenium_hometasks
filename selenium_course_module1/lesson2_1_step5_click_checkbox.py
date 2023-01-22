from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from webdriver_manager.chrome import ChromeDriverManager

url = "https://suninjuly.github.io/math.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(url)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)

	answer_aria = browser.find_element(By.ID, "answer")
	answer_aria.send_keys(y)

	robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
	robot_checkbox.click()

	robot_radiobutton = browser.find_element(By.ID, "robotsRule")
	robot_radiobutton.click()

	submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
	submit.click()

finally:
	time.sleep(30)
	browser.quit()



