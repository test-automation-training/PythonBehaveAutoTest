import time
import chromedriver_binary as chrome
from selenium import webdriver

driver = webdriver.Chrome(chrome.chromedriver_filename)
driver.get("http://www.bing.com")
driver.maximize_window()
driver.find_element_by_id("sb_form_q").send_keys("game")
# driver.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)

driver.find_element_by_id("sb_go_par").click()
assert driver.title.__contains__('game')
time.sleep(3)
# driver.find_element_by_link_text('msn free games').click()
# time.sleep(3)
driver.quit()
