from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)

select = driver.find_element(By.LINK_TEXT, value='Electronics')
select.click()
time.sleep(2)

select_1 = driver.find_element(By.LINK_TEXT, value='Audio')
select_1.click()
time.sleep(2)

driver.close()