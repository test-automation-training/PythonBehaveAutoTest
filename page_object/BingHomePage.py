# 打开页面
def open(context):
    context.driver.get('http://www.bing.com')
    context.driver.maximize_window()

# Bing搜索框元素
def search_textbox(context):
    return context.driver.find_element_by_id('sb_form_q')

# 提交按钮
def submit_button(context):
    return context.driver.find_element_by_id('sb_go_par')

# 登录链接
def sign_in_link(context):
    return context.driver.find_element_by_id('id_s')
