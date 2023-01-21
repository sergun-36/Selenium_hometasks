from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


url = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()

browser.get(url)

x = browser.find_element(By.ID, 'input_value').text
result = str(math.log(abs(12*math.sin(int(x)))))

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(result)


checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()



radio_robot_rules = browser.find_element(By.ID, 'robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', radio_robot_rules)
radio_robot_rules.click()

submit = browser.find_element(By.TAG_NAME, 'button')#(By., 'button[type = "submit"]')
submit.click()


time.sleep(5)
browser.quit()
