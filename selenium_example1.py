import chromedriver_binary as chrome
from selenium import webdriver

driver = webdriver.Chrome(chrome.chromedriver_filename)
# driver = webdriver.Firefox(executable_path = "driver/geckodriver")
driver.get("http://www.bing.com")
driver.maximize_window()
driver.quit()
# driver.close()
