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

driver.find_element(By.XPATH, value="//input[@id='twotabsearchtextbox']").send_keys('iphones')
time.sleep(5)
driver.find_element(By.XPATH, value="//input[@id='nav-search-submit-button']").click()
time.sleep(5)

lists = driver.find_elements(By.XPATH, value="//span[@class='a-size-medium a-color-base a-text-normal']")

print(str(len(lists)) + ' products found')

for i in lists:
    print(i.text)
# xpath.send_keys('iphones')
# time.sleep(3)
driver.close()
