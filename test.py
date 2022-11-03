from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

driver.get("http://www.ecosia.org")
driver.implicitly_wait(2)
driver.find_element(By.NAME, value="q").send_keys("Test Automation")
driver.find_element(By.NAME, value="q").send_keys(Keys.ENTER)

