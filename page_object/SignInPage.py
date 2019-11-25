from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 用户名输入框
def username_textbox(context):
    # 下面方法是一个典型的等待机制，因为Bing登录页面用户名输入框有一个动画效果，立即输入会导致测试不稳定，需要等待元素可以输入时再操作
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable((By.ID, "i0116")))
    return context.driver.find_element_by_id('i0116')

# 提交按钮
def submit_button(context):
    return context.driver.find_element_by_id('idSIButton9')


def password_textbox(context):
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable((By.ID, "i0118")))
    return context.driver.find_element_by_id('i0118')
