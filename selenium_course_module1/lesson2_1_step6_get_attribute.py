from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

url = "https://suninjuly.github.io/math.html"
expected_checked_value = "true"

try:
	browser = webdriver.Chrome(ChromeDriverManager().install())
	browser.get(url)

	people_radio = browser.find_element(By.ID, "peopleRule")
	people_checked = people_radio.get_attribute("checked")
	print(people_checked)
	assert people_checked is not None, "People radio is not selected by default"
	assert people_checked == expected_checked_value, "People radio is not selected by default"

	robots_radio = browser.find_element(By.ID, "robotsRule")
	robots_checked = robots_radio.get_attribute("checked")
	assert robots_checked is None, "Robot radio button is selected by default"
finally:
	time.sleep(5)
	browser.quit()
