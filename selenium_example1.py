import chromedriver_binary as chrome
from selenium import webdriver

# 初始化浏览器，不同浏览器类型参考Selenium文档
driver = webdriver.Chrome(chrome.chromedriver_filename)
# driver = webdriver.Firefox(executable_path = "driver/geckodriver")

# 打开网址
driver.get("http://www.bing.com")

# 最大化窗口
driver.maximize_window()

# 关闭窗口
driver.quit()
# driver.close()
