from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://opensea.io/")

explore_bt = driver.find_element_by_class_name("gMiESj").click()
time.sleep(1)
input_input_min = driver.find_element(By.XPATH, '//input[@data-testid="Input"]')
input_input_min.clear()
input_input_min.send_keys("500")
input_input_min.send_keys(Keys.RETURN)

apply_bt = driver.find_element_by_class_name("kmCSYg").click()

# input_search_field2 = driver.find_element_by_xpath("//input[@type=’search’]")

# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# element = driver.find_element_by_id("id-search-field")
time.sleep(10)

driver.close()