from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Username_TextBox(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "i0116")))
    return context.driver.find_element_by_id('i0116')

def Submit_Button(context):
    return context.driver.find_element_by_id('idSIButton9')

def Password_TextBox(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "i0118")))
    return context.driver.find_element_by_id('i0118')