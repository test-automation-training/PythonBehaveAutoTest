from selenium import webdriver
import time
import log
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
#logging.debug('open browser')
driver.get("http://www.bing.com")
driver.maximize_window()

#driver.save_screenshot('screenshot/homepage.png')

driver.find_element_by_id("sb_form_q").send_keys("game")

#WebDriverWait(driver,10).until(EC.presence_of_all_elements_located)
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "sb_go_par")))

driver.find_element_by_id("sb_go_par").click()
time.sleep(3)

driver.quit()