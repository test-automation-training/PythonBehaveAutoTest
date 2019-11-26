import time
import chromedriver_binary as chrome
from selenium import webdriver

driver = webdriver.Chrome(chrome.chromedriver_filename)
# logging.debug('open browser')
driver.get("http://www.bing.com")
driver.maximize_window()

# driver.save_screenshot('screenshot/homepage.png')

driver.find_element_by_id("sb_form_q").send_keys("game")
# 下面是等待机制，等待某个元素满足特定条件
# WebDriverWait(driver,10).until(EC.presence_of_all_elements_located)
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "sb_go_par")))

driver.find_element_by_id("sb_go_par").click()
time.sleep(3)

driver.quit()
