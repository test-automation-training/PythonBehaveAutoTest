import time
import chromedriver_binary as chrome
from selenium import webdriver

driver = webdriver.Chrome(chrome.chromedriver_filename)
driver.get("http://www.bing.com")
driver.maximize_window()

# 获取页面元素并输入值
driver.find_element_by_id("sb_form_q").send_keys("game")
# driver.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)

#获取页面元素并点击
driver.find_element_by_id("sb_go_par").click()

#断言页面title包含特定文本
assert driver.title.__contains__('game')

# sleep3秒，慎用
time.sleep(3)
# driver.find_element_by_link_text('msn free games').click()
# time.sleep(3)
driver.quit()
