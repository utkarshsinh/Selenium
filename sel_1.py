from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
search_bar = driver.find_element(By.NAME, value='q')
search_bar.clear()
search_bar.send_keys("Selenium")
time.sleep(5)
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.refresh()
driver.close()