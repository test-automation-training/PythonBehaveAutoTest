def open(context):
    context.driver.get('http://www.bing.com')
    context.driver.maximize_window()


def search_textbox(context):
    return context.driver.find_element_by_id('sb_form_q')


def submit_button(context):
    return context.driver.find_element_by_id('sb_go_par')


def sign_in_link(context):
    return context.driver.find_element_by_id('id_s')
