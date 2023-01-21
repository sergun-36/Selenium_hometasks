import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#additional argument  https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView

url = 'https://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(url)

button = browser.find_element(By.TAG_NAME, 'button')
#button.click()
browser.execute_script('return arguments[0].scrollIntoView(true);', button)

button.click()

time.sleep(6)
browser.quit()

"""
example JS scripts

// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);

scroll 100px down

browser.execute_script("window.scrollBy(0, 100);")
"""